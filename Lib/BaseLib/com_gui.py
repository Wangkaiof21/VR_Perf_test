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
from tkinter import font as tk_font
from tkinter.filedialog import askdirectory
import zipfile
import subprocess

import os
from Lib.BaseLib.LogMessage import LogMessage, LOG_ERROR, LOG_RUN_INFO
import tkinter
from Lib.BaseLib.com_power_wash_model import PowerWashPerfData, get_func_name
# 检查关键字的存储列表
selection_list = list()


class MyGUI:
    def __init__(self, init_window_):
        """
        self=TK().host_label.grid
        :param init_window_:
        """
        lab_row = 0
        self.init_window = init_window_
        self.font_type = tk_font.Font(family='Fixdsys', size=10, weight=tk_font.BOLD)
        self.init_window.title("性能数据分析脚本0.1版")  # 窗口名
        # self.init_window_name.geometry('320x140+10+10')      #290 140为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        # self.init_window.geometry('800x800+620+40')
        self.init_window.geometry('500x600+620+40')

        # 第一行
        label_row = 0
        # step1 设置位置 实例化了一个Label
        self.host_label = Label(self.init_window, font=self.font_type)
        # 使用grid布局器 进行性网格划分
        self.host_label.grid(row=label_row, column=0, sticky=E, padx=5, pady=12)
        # step2 设置输入框的类别 和填充基本内容

        # 解析文件地址
        self.ten_lable = Label(self.init_window, text="CSV地址", font=self.font_type, width=14, anchor=NE)
        self.ten_lable.grid(row=lab_row, column=0, sticky=E)
        default_ten = StringVar()
        default_ten.set('C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\perf_data\\VR_PW_FULL_data')
        self.en_tenant = Entry(self.init_window, width=15, textvariable=default_ten)
        self.en_tenant.grid(row=lab_row, column=1, padx=3, pady=9)

        # 图片生成地址
        self.env_lable = Label(self.init_window, text="图片存放地址", font=self.font_type, width=14, anchor=NE)
        self.env_lable.grid(row=lab_row, column=2, sticky=E)
        default_env = StringVar()
        default_env.set('C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\power_wash_image')
        self.en_env = Entry(self.init_window, width=15, textvariable=default_env)
        self.en_env.grid(row=lab_row, column=3, padx=3, pady=9)
        # 勾选项目 /list
        self.test_case_index = ['cpu_utilization_percentage', 'app_pss_MB', 'app_uss_MB',
                                'battery_level_percentage',
                                'average_frame_rate', 'cpu_level', 'gpu_level', 'Time Stamp']

        self.v_list = []
        self.variable = IntVar()
        self.select_all = Radiobutton(self.init_window, text="全选", variable=self.variable, value=1,
                                      command=self.check_list)
        self.reverse_selection = Checkbutton

    def check_list(self):
        list_type = self.variable.get()
        if list_type == 1:
            LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f'Selected: {self.name}')
            if all([])


def main():
    LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"----------开始分析...----------")
    init_window = Tk()  # 实例化出一个父窗口
    gui = MyGUI(init_window)
    # 设置根窗口默认属性
    init_window.mainloop()
    # mainloop()=主事件循环
    # mainloop()函数接受到事件，判断是单击按钮，发给按钮，按钮调用指定的事件函数，
    # 修改label的属性text后，label自动调用自己的显示函数show(),重新显示自己。这是程序运行的基本方式
    LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"----------分析结束...----------")


if __name__ == '__main__':
    main()
