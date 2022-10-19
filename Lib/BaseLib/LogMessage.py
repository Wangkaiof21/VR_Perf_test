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
LOG_RUN_INFO = 70
logging.addLevelName(LOG_RUN_INFO, 'RUN_INFO')

# 日志打印等级
_LEVEL_COLOR = {
    LOG_DEBUG: Fore.BLUE,
    LOG_INFO: Fore.WHITE,
    LOG_WARN: Fore.YELLOW,
    LOG_ERROR: Fore.RED,
    LOG_SYS: Fore.GREEN,
    # 由于logger.setLevel(LOG_DEBUG) 不起效，额外设定等级方便打印
    # 这里不会打印level=30以上的log
    LOG_RUN_INFO: Fore.CYAN,
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
    # logger.setLevel(LOG_DEBUG)
    time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    caller = ""
    if level == LOG_ERROR or level == LOG_WARN or level == LOG_INFO:
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
        [f'{color}{time_}\t{level_name}\t[{module}]\t{row}{caller}{Style.RESET_ALL}' for row in str(msg).split("\n")])
    logger.log(level, log_msg)

