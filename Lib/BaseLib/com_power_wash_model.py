import os
import re
import sys
import inspect
from LogMessage import LogMessage, LOG_INFO, LOG_ERROR,LOG_DEBUG
from com_msg_center import MsgCenter

# MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
# MsgCenter(MODULE_NAME,level=LOG_DEBUG)


def get_func_name():
    return inspect.stack()[1][3]


class PowerWashPerfData:
    def __init__(self, base_dir, file_num):
        self.index = file_num
        self.file_path = base_dir if os.path.exists(base_dir) else LogMessage(level=LOG_ERROR, module=get_func_name(),
                                                                              msg="data path dose not exist")
        self.perf_data_path = os.path.join(self.file_path, str(self.index))
        # self.TSV_INDEX = ["Processor Time", "Handle Count", "Private Bytes", "Virtual Bytes", "Working Set",
        #                   "Working Set - Private"]

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
            break
        return files_

    def get_vr_csv_data(self, fp: str, split_num_start: int, split_num_end: int) -> dict:
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
        test_project_name = os.path.abspath(os.path.join(fp, "..")).split("\\")[-1]
        lines = list()
        try:
            with open(fp, "r", encoding="utf-8") as r:
                vr_data_lines = r.read().split("\n")
                vr_index = vr_data_lines[0].split(",")
                for vr_data in vr_data_lines[1:]:
                    line = dict(zip(vr_index, [int(x) for x in vr_data.split(",")]))
                    lines.append(line)
                    LogMessage(level=LOG_INFO, module=get_func_name(), msg=f"Data => {line}")

        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"Error => {e}")
        # file = dict()
        # for k, v in file_datas.items():
        #     fps = list()
        #     cpu = list()
        #     pss = list()
        #     uss = list()
        #     battery_ = list()
        #     date_ = list()
        #     clean_datas = dict()
        #     for line in self.VR_INDEX:
        #         clean_datas[line] = ""
        #     for line in v:
        #         date_.append(line.get(TIME_STAMP))
        #         fps.append(line.get(FPS_))
        #         pss.append(line.get(PSS_MEMORY))
        #         uss.append(line.get(USS_MEMORY))
        #         cpu.append(line.get(CPU_USED))
        #         battery_.append(line.get(BATTERY_PERCENT))
        #     clean_datas[FPS_] = fps
        #     clean_datas[PSS_MEMORY] = pss
        #     clean_datas[USS_MEMORY] = uss
        #     clean_datas[CPU_USED] = cpu
        #     clean_datas[BATTERY_PERCENT] = battery_
        #     clean_datas[TIME_STAMP] = date_
        #     file[k] = clean_datas
        # for case_name, value_dict in file.items():
        #     # login数据不需要更改
        #     if case_name == "login":
        #         break
        #     else:
        #         file.get(case_name)[CPU_USED] = file.get(case_name).get(CPU_USED)[50:-20]
        #         file.get(case_name)[FPS_] = file.get(case_name).get(FPS_)[50:-20]
        #         file.get(case_name)[PSS_MEMORY] = file.get(case_name).get(PSS_MEMORY)[50:-20]
        #         file.get(case_name)[USS_MEMORY] = file.get(case_name).get(USS_MEMORY)[50:-20]
        #         file.get(case_name)[TIME_STAMP] = file.get(case_name).get(TIME_STAMP)[50:-20]
        #         file.get(case_name)[BATTERY_PERCENT] = file.get(case_name).get(BATTERY_PERCENT)[50:-20]
        # 原始数据 对比用
        # file.get(case_name)[CPU_USED] = file.get(case_name).get(CPU_USED)
        # file.get(case_name)[FPS_] = file.get(case_name).get(FPS_)
        # file.get(case_name)[PSS_MEMORY] = file.get(case_name).get(PSS_MEMORY)
        # file.get(case_name)[USS_MEMORY] = file.get(case_name).get(USS_MEMORY)
        # file.get(case_name)[TIME_STAMP] = file.get(case_name).get(TIME_STAMP)
        # file.get(case_name)[BATTERY_PERCENT] = file.get(case_name).get(BATTERY_PERCENT)
        return dict()


pw = PowerWashPerfData(base_dir="C:\\Users\\Administrator\Desktop\\vr_\\VR_Perf_test\\perf_data\\VR_PW_data",
                       file_num=20221018)
pw.get_file_data()
