import logging
from colorama import Fore, Style
import os
import sys
import time

TIMER_FLAG = False

# 定义打印等级
LOG_DEBUG = logging.DEBUG
LOG_INFO = logging.INFO
LOG_WARN = logging.WARN
LOG_ERROR = logging.ERROR
LOG_SYS = 90
logging.addLevelName(LOG_SYS, 'SYS')

# 日志打印等级
_LEVEL_COLOR = {
    LOG_DEBUG: Fore.BLUE,
    LOG_INFO: Fore.WHITE,
    LOG_WARN: Fore.YELLOW,
    LOG_ERROR: Fore.RED,
    LOG_SYS: Fore.GREEN,
}


def LogMessage(level=LOG_INFO, module="NA", msg="NA", logger_name="Test_Message"):
    """
    :param level: logger级别
    :param module: logger模块前缀
    :param msg: logging信息
    :param logger_name: 全局可注册多个不同名logger
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    caller = ""
    if level == LOG_ERROR or level == LOG_WARN:
        """
        从调用堆栈返回一个框架对象。 如果给定了可选的整数深度，则返回堆栈顶部以下多次调用的框架对象。
        如果这比调用堆栈更深，则会引发 ValueError。 深度的默认值为零，返回调用堆栈顶部的帧。
        sys._getframe() 带下划线的方法属于cpython的东西 在不同平台有不同实现 .f_back 也一样
        """
        # 获取当前调用的信息 返回类型为框架类型
        f_back = sys._getframe().f_back
        # 调用的函数名
        co_name = f_back.f_code.co_name
        # 调用文件名
        file_name = os.path.basename(f_back.f_code.co_filename)
        # 调用者所在的行数
        line_no = f_back.f_lineno
        caller = f"\t[{co_name}:{file_name}-{line_no}]"
    level_name = logging.getLevelName(level)
    color = _LEVEL_COLOR.get(level)
    log_msg = "\n".join(
        [f'{color}{t}\t{level_name}\t[{module}]\t{row}{caller}{Style.RESET_ALL}' for row in str(msg).split("\n")])
    logger.log(level, log_msg)

# import logging
# from logging import handlers
#
#
# class Logger(object):
#     level_relations = {
#         'debug': logging.DEBUG,
#         'info': logging.INFO,
#         'warning': logging.WARNING,
#         'error': logging.ERROR,
#         'crit': logging.CRITICAL
#     }  # 日志级别关系映射
#
#     def __init__(self, filename, level='info', when='D', backCount=3,
#                  fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
#         self.logger = logging.getLogger(filename)
#         format_str = logging.Formatter(fmt)  # 设置日志格式
#         self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
#         sh = logging.StreamHandler()  # 往屏幕上输出
#         sh.setFormatter(format_str)  # 设置屏幕上显示的格式
#         th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
#                                                encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
#         # 实例化TimedRotatingFileHandler
#         # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
#         # S 秒
#         # M 分
#         # H 小时、
#         # D 天、
#         # W 每星期（interval==0时代表星期一）
#         # midnight 每天凌晨
#         th.setFormatter(format_str)  # 设置文件里写入的格式
#         self.logger.addHandler(sh)  # 把对象加到logger里
#         self.logger.addHandler(th)
#
#
# if __name__ == '__main__':
#     log = Logger('all.log', level='debug')
#     log.logger.debug('debug')
#     log.logger.info('info')
#     log.logger.warning('警告')
#     log.logger.error('报错')
#     log.logger.critical('严重')
#     Logger('error.log', level='error').logger.error('error')
