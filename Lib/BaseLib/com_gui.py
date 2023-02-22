# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import mysql.connector

from mysql.connector import errorcode
import json
import os
import time
import datetime
import logging
from logging.handlers import RotatingFileHandler
import chardet
import shutil
import re
import pymysql
import socket
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter.filedialog import askdirectory
import zipfile
import subprocess

import os
from Lib.BaseLib.LogMessage import LogMessage, LOG_ERROR, LOG_RUN_INFO
import tkinter
from Lib.BaseLib.com_power_wash_model import PowerWashPerfData, get_func_name


class MY_GUI():
    def __init__(self, init_window_name):
        lab_row = 0
        self.init_window = init_window_name
        self.ft = tkFont.Font(family='System', size=10, weight=tkFont.BOLD)
        self.init_window.title("性能数据分析脚本0.1版")  # 窗口名
        # self.init_window_name.geometry('320x140+10+10')      #290 140为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window.geometry('800x800+620+40')


def main():
    LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"----------开始分析...----------")
    init_window = Tk()  # 实例化出一个父窗口
    gui = MY_GUI(init_window)
    # 设置根窗口默认属性
    init_window.mainloop()
    # mainloop()函数接受到事件，判断是单击按钮，发给按钮，按钮调用指定的事件函数，
    # 修改label的属性text后，label自动调用自己的显示函数show(),重新显示自己。这是程序运行的基本方式
    LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"----------分析结束...----------")


if __name__ == '__main__':
    main()
