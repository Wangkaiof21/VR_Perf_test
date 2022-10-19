import os
import re
import sys
import inspect
import numpy as np
from LogMessage import LogMessage, LOG_ERROR, LOG_RUN_INFO
from com_msg_center import MsgCenter
import random

# MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
# MsgCenter(MODULE_NAME,level=LOG_DEBUG)
np.set_printoptions(threshold=np.inf)


def get_func_name():
    return inspect.stack()[1][3]


class PowerWashPerfData:
    def __init__(self, base_dir, file_num):
        self.index = file_num
        self.file_path = base_dir if os.path.exists(base_dir) else LogMessage(level=LOG_ERROR, module=get_func_name(),
                                                                              msg="data path dose not exist")
        self.perf_data_path = os.path.join(self.file_path, str(self.index))
        self.VR_INDEX = ['cpu_utilization_percentage', 'app_pss_MB', 'app_uss_MB', 'battery_level_percentage',
                         'average_frame_rate']

    def get_file_data(self):
        """
        解析文件，把文件数据处理成合适的结构
        :return:
        """
        files_ = list()
        try:
            for test_file in os.listdir(self.perf_data_path):
                test_file_dir = os.path.join(self.perf_data_path, test_file)
                for root, dirs, files in os.walk(test_file_dir):
                    if not os.listdir(root):
                        # 如果文件夹为空 则跳过
                        break
                    for file_name in files:
                        file_full_dir = os.path.join(root, file_name)
                        files_.append(file_full_dir)
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"File error --> {e} !!!")
        for file in files_:
            data = self.get_vr_csv_data(file, split_num_start=0, split_num_end=0)
            # data = self.get_vr_csv_data(file, split_num_start=1, split_num_end=10)
            break
        return files_

    def get_vr_csv_data(self, fp: str, split_num_start: int, split_num_end: int) -> list:
        """
        从绝对路径获取一体机数据，返回字典的形式
        这边要特殊处理 login文档的数据保留全的
        其他的要去掉头部login时间和尾部的退出程序时间
        :param fp:
        :param split_num_start:切割量的头
        :param split_num_end:切割量的尾
        :return:
        """
        if not os.path.exists(fp):
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg="file is None")
        # test_project_name = os.path.abspath(os.path.join(fp, "..")).split("\\")[-1]
        lines = list()
        result = list()
        try:
            with open(fp, "r", encoding="utf-8") as r:
                vr_data_lines = r.read().split("\n")
                vr_index = vr_data_lines[0].split(",")
                # for vr_data in vr_data_lines[1:]:
                #     line = dict(zip(vr_index, [int(x) for x in vr_data.split(",")]))
                #     lines.append(line)
                lines.append(vr_index)
                for vr_data in vr_data_lines[1:]:
                    line = [int(x) for x in vr_data.split(",")]
                    lines.append(line)
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"Error => {e}")
        lines = np.array(lines).T
        lines_copy = lines.tolist()
        # 反转数组 且转换为一般list
        wash_lines = list()
        for index in range(len(lines_copy)):
            if lines_copy[index][0] in self.VR_INDEX:
                wash_lines.append(lines_copy[index])
        test_num = random.randint(0, len(wash_lines))
        if split_num_start > len(wash_lines[test_num]) or split_num_end > len(wash_lines[test_num]):
            LogMessage(level=LOG_ERROR, module=get_func_name(),
                       msg=f"split_num {split_num_start}, split_num {split_num_end} out of the range")
        try:
            for line in wash_lines:
                line_ = dict()
                key, val = line[0], [int(x) for x in line[1:]]
                if split_num_start and split_num_end:
                    line_[key] = val[split_num_start:split_num_end]
                    LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"Data => {line_}")
                    result.append(line_)
                else:
                    line_[key] = val
                    LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"Data => {line_}")
                    result.append(line_)
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"Error => {e}")
        return result


pw = PowerWashPerfData(base_dir="C:\\Users\\Administrator\Desktop\\vr_\\VR_Perf_test\\perf_data\\VR_PW_data",
                       file_num=20221018)
pw.get_file_data()
