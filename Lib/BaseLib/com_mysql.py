"""
sql压测
"""
import time
import argparse
from multiprocessing import Process, Queue, Manager, Value
import pymysql
from faker import Faker
import random
import signal
import sys
from LogMessage import LogMessage, LOG_WARN, LOG_INFO, LOG_ERROR

"""
数据库压测
使用faker制造假数据往数据库里面插入假数据

"""

VERSION = "0.1"


def get_connect(sql_host, sql_port, sql_user, sql_password, sql_db_name):
    """
    制造一个数据库对象，进行游标操作
    :param sql_host:
    :param sql_port:
    :param sql_user:
    :param sql_password:
    :param sql_db_name:
    :return:
    """
    connect_ = pymysql.connect(
        host=sql_host,
        port=sql_port,
        user=sql_user,
        password=sql_password,
        database=sql_db_name
    )
    return connect_


def insert_table(sql_host, sql_port, sql_user, sql_pass_word, db_name, action, table_base_name, tab_rows,
                 table_per_commit,
                 table_thread, log_, table_count, p, q):
    """

    :param sql_host:
    :param sql_port:
    :param sql_user:
    :param sql_pass_word:
    :param db_name:
    :param action:
    :param table_base_name:
    :param tab_rows:
    :param table_per_commit:
    :param table_thread:
    :param log_:
    :param table_count:
    :param p:
    :param q:
    :return:
    """
    fake = Faker()
    connect_ = get_connect(sql_host, sql_port, sql_user, sql_pass_word, db_name)
    cursor = connect_.cursor()
    if log_:
        cursor.execute("set session sql_log_bin=1")
    else:
        cursor.execute("set session sql_log_bin=0")
    while True:
        try:
            table_index = str(q.get(block=False, timeout=10))
        except Exception as e:
            LogMessage(level=LOG_ERROR, module="insert_table", msg=f"Error => {e}")
            break
        if int(table_index) > int(table_count):
            break
        table_name = str(table_base_name) + str(table_index)
        LogMessage(level=LOG_INFO, module='insert_table', msg=f'process: {p} 往 {table_name} 插入 {tab_rows} 行... ')
        rest_of_rows = tab_rows
        while rest_of_rows > 0:
            run_rows = table_per_commit if rest_of_rows > table_per_commit else rest_of_rows
            values = ""
            for x in range(0, run_rows):
                k = random.randint(1, tab_rows - 20)
                values += ",('{k}','{c}','{c2}')".format(k=random.randint(1, tab_rows - 20), c=fake.text(100),
                                                         c2=fake.text(50))
            sql = f"insert into {table_name}(k,c,c2) values{values[1:]}"
            # sql = "insert into {table_name}(k,c,c2) values{values}".format(table_name=table_name, values=values[1:])
            cursor.execute("begin;")
            cursor.execute(sql)
            cursor.execute("commit")
            rest_of_rows -= table_per_commit
        # 本来想顺便把索引创建了的 结果会产生metadata look 锁 ，原因是建表后没提交 虽然其他表能查到索引和数据


def _argparse():
    """
    argparse.ArgumentParser创建一个命令行参数对象
    add_argument 往参数对象里面添加参数
    parse_args 解析参数对象获得解析对象
    :return:
    add_argument参数
    name or flags ： 一个命名或者 一个选项字符串的列表
    action ：表示该选项要执行的操作
    default ： 当参数未在命令行中出现时使用的值
    dest ： 用来指定参数的位置
    type ：为参数类型，例如int
    choices ： 用来选择输入参数的范围。例如choice = [1, 5, 10], 表示输入参数只能为1,5 或10
    help ： 用来描述这个选项的作用
    """
    parser_ = argparse.ArgumentParser(description='Mysql 压测脚本')
    # parser.add_argument('--type',  action='store', dest='db_type', default='mysql', help='数据库类型(目前只支持Mysql)')
    parser_.add_argument('--host', action='store', dest='host', default='127.0.0.1', help='数据库服务器地址. default 127.0.0.1')

    parser_.add_argument('--port', '-P', action='store', dest='port', default=3306, type=int,
                         help='数据库端口. default 3306')
    parser_.add_argument('--user', '-u', action='store', dest='user', default="root", help='数据库用户')
    parser_.add_argument('--password', '-p', action='store', dest='password', help='数据库密码')
    parser_.add_argument('--db-name', '-D', action='store', dest='dbname', help='数据库名字')
    parser_.add_argument('--version', '-v', '-V', action='store_true', dest="version", help='VERSION')
    parser_.add_argument(action='store', dest='action', nargs='?', default='prepare', help='prepare|run|cleanup')
    parser_.add_argument('--table-count', '-t', action='store', dest='table_count', default=12, type=int,
                         help='表的数量 默认12')
    parser_.add_argument('--table-name', '-Tname', action='store', dest='table_name', default="ddcw", type=str,
                         help='表的名字 默认ddcw')
    parser_.add_argument('--table-rows', '-Trows', action='store', dest='table_rows', default=100000, type=int,
                         help='每张表有多少行 默认100K')
    parser_.add_argument('--insert-per-commit', '-i', action='store', dest='insert_per_commit', default=1000, type=int,
                         help='准备数据的时候, 多少次insert后再commit(只有prepare阶段才有效) 默认1000')
    parser_.add_argument('--log', '-l', action='store_true', dest='log', help='准备数据的时候, 是否写日志(默认不写)')
    parser_.add_argument('--report-interval', '-ri', action='store', dest='report_interval', default=10, type=int,
                         help='多少秒显示一次结果(默认10)')
    parser_.add_argument('--thread', '-T', action='store', dest='thread', default=8, type=int, help='并行度(默认8)')
    parser_.add_argument('--run-time', '-r', action='store', dest='runtime', default=120, type=int,
                         help='运行时间(单位:秒)(默认120)')
    parser_.add_argument('--mode', '-m', action='store', dest='mode', choices=[0, 1, 2], default=0, type=int,
                         help='0 读写混合(2u + 1d + 1i + 14s)   1 仅读   2 仅写  (默认0)')
    args = parser_.parse_args()
    return args


def main(host, port, user, passwd, db_name, action, table_base_name, table_rows, table_per_commit, table_thread, log,
         runtime, report_interval, table_count, mode, ):
    """
    事务参考sysbench
    读写混合事务 只读+只写
    :param host:
    :param port:
    :param user:
    :param passwd:
    :param db_name:
    :param action:动作
    :param table_base_name:表名
    :param table_rows:每张表的数据量
    :param table_per_commit:
    :param table_thread:
    :param log:
    :param runtime:
    :param report_interval:
    :param table_count:表数量
    :param mode:0 读写  1 仅读  2仅写
    :return:
    """
    conn = get_connect(sql_host=host, sql_port=port, sql_user=user, sql_password=passwd, sql_db_name=db_name)
    cursor = conn.cursor()
    if action == "prepare":
        LogMessage(level=LOG_INFO, module="mian", msg="开始创建")
        for table_index in range(1, table_count + 1):
            table_name = f"{table_base_name}{table_index}"
            cursor.execute(f'''
  CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` int(11) NOT NULL DEFAULT '0',
  `c` char(120) NOT NULL DEFAULT '',
  `c2` char(60) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) /*! ENGINE = innodb */
/*!*/;
			''')
            LogMessage(level=LOG_INFO, module="main", msg=f"make table {db_name}.{table_name} success!")
            cursor.execute(f"select count(*) from {db_name}.{table_name}")
            if int(cursor.fetchall()[0][0]) > 0:
                LogMessage(level=LOG_ERROR, module="main", msg=f"{db_name}.{table_name} 已存在数据, 请先清空, 或者换个名字!")
                sys.exit(1)
            # 这里不加commit的话, 多进程最后一张表就无法创建索引
            cursor.execute("commit")
            queue = Queue(table_count * 2)
            for index in range(1, table_count * 2 + 1):
                queue.put(index)


if __name__ == '__main__':
    # def quit(signum, frame):
    #     print("被手动停止了..")
    #     sys.exit(2)
    #
    #
    # signal.signal(signal.SIGINT, quit)
    #
    # # 解析参数
    # parser = _argparse()
    # if parser.version:
    #     print("Version: {VERSION}".format(VERSION=VERSION))
    # else:
    #     main(parser.host, parser.port, parser.user, parser.password, parser.dbname, parser.action, parser.table_name,
    #          parser.table_rows, parser.insert_per_commit, parser.thread, parser.log, parser.runtime,
    #          parser.report_interval, parser.table_count, parser.mode)
    parser = _argparse()
    if parser.version:
        LogMessage(level=LOG_WARN, module="main", msg=f"Version:{VERSION}")
    else:
        main(parser.host)
