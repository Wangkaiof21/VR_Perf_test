import sys
import psutil
import os
from Lib.BaseLib.LogMessage import LogMessage, LOG_INFO, LOG_ERROR

"""
需求：
在一段时间内通过sys.args【2】获取入参
进入记录状态 记录初始的电脑状态，多少运行中的程序，占有的cpu，内存信息
然后把运行程序后的一段时间内的cpu信息和内存信息记录
"""

# INDEX = sys.argv[1]


class CPUData:
    def __init__(self, process_name=None):
        self.p_name = process_name
        # self.switch = INDEX if isinstance(INDEX, int) else print("please check input!")

    def get_process(self):
        """
        获取当前系统所有进程id列表
        获取当前被测进程的pid
        :return:
        """
        all_pids = psutil.pids()
        pid_lst = []
        try:
            # 遍历所有进程，名称匹配的加入process_lst
            for pid in all_pids:
                pid_ = psutil.Process(pid)
                if self.p_name is None:
                    LogMessage(level=LOG_ERROR, msg="please check process_name", module="get_process")
                    break
                else:
                    if pid_.name() == self.p_name:
                        # p = psutil.Process(pid)
                        pid_lst.append(pid_)
        except Exception as e:
            LogMessage(level=LOG_ERROR, msg=f"func get_process error => {e}", module="get_process")

        return all_pids

    def get_cpu_line(self):
        true_core = psutil.cpu_count()
        fake_core = psutil.cpu_count(logical=False)
        while True:
            # if self.switch == 0:
            #     break
            # cpu占有率 可能要转换
            one_second_cpu_line = psutil.cpu_percent(interval=1, percpu=True)
            # 物理内存信息
            one_second_virtual_memory_line = psutil.virtual_memory()
            # 交换内存信息
            one_second_swap_memory_line = psutil.swap_memory()
            print(one_second_cpu_line)
            print(one_second_virtual_memory_line)
            print(one_second_swap_memory_line)


cpu = CPUData("")
# data = cpu.get_process()

cpu.get_cpu_line()
