"""
需求：
需要一个筛选出固定名字文档的模块，
需要一个读取csv，tsv文件的模块
需要一个数据处理模块
需要一个图形处理模块
"""

import os
import sys
import openpyxl
from LogMessage import LogMessage, LOG_INFO, LOG_ERROR
import matplotlib

HANDLE_COUNT = 'Handle Count'
PRIVATE_BYTES = 'Private Bytes'
PROCESSOR_TIME = 'Processor Time'
VIRTUAL_BYTES = 'Virtual Bytes'
WORKING_SET = 'Working Set'
WORKING_SET_PRIVATE = 'Working Set - Private'


class PerfData:
    def __init__(self, fp, index=None):
        """

        :param fp:
        :param index:
        """
        self.base_dir = fp if os.path.exists(fp) else LogMessage(level=LOG_ERROR, module="get_tsv_data",
                                                                 msg="path dose not exist")
        self.file_path = os.path.join(self.base_dir, "PC_Perf_data") if index == "pc" else os.path.join(self.base_dir,
                                                                                                        "VR_Perf_data")
        self.TSV_INDEX = ["Processor Time", "Handle Count", "Private Bytes", "Virtual Bytes", "Working Set",
                          "Working Set - Private"]

    def get_file_collector(self) -> list:
        """
        获取被测文件绝对路径列表
        :return:
        """
        test_collector = list()
        try:
            for test_file in os.listdir(self.file_path):
                test_file_dir = os.path.join(self.file_path, test_file)
                files_ = list()
                for root, dirs, files in os.walk(test_file_dir):
                    for file_name in files:
                        if "DataCollector" in file_name or "fps" in file_name:
                            file_full_dir = os.path.join(root, file_name)
                            files_.append(file_full_dir)
                            # LogMessage(level=LOG_ERROR, module="get_file_path", msg=f"Error => {file_full_dir}")
                test_collector.append(files_)
        except Exception as e:
            LogMessage(level=LOG_ERROR, module="get_file_path", msg=f"Error => {e}")
        return test_collector

    def get_data_structure(self) -> list:
        """
        分别从里面取出tsv，csv数据，整理成数据结构，不足的补0，缺失的置为0
        :return:
        """
        test_case_ = list()
        file_lines = self.get_file_collector()
        for files in file_lines:
            "从分离出csv和tsv tsv是性能数据 csv是fps数据 这个是按组来计算的"
            test_case_datas = dict()
            for index in range(len(files)):
                if os.path.basename(files[index]).split(".")[-1] == "tsv":
                    tsv_datas = self.get_tsv_data(files[index])
                    test_case_datas["tsv_data"] = tsv_datas
                elif os.path.basename(files[index]).split(".")[-1] == "csv":
                    csv_datas = self.get_csv_data(files[index])
                    test_case_datas["csv_data"] = csv_datas
            test_case_.append(test_case_datas)
        return test_case_

    def get_tsv_data(self, fp: str) -> dict:
        """
        获取tsv数据内容 新版功能数据
        tsv 数据长这样"1491"，可能先需要strip()掉
        :param fp:
        :return:dict
        """
        if not os.path.exists(fp):
            LogMessage(level=LOG_ERROR, module="get_tsv_data", msg="file is None")
            # return None
        dir_name = os.path.abspath(os.path.join(fp, "..")).split("\\")[-1]
        tsv_file_datas = dict()
        file_lines = list()
        try:
            with open(fp, "r", encoding="utf-8") as r:
                tsv_data = r.read()
                tsv_data = tsv_data.split("\n")
                for lines in tsv_data[1:-1]:
                    # 切割转换的时候要把双引号去掉
                    lines = [x.strip('"') for x in lines.split("\t")]
                    # 去掉时间戳列 和把空的数字用0替换
                    lines = ['0.00' if x == ' ' else x for x in lines[1:]]
                    # 要保留int类型数据，要保留小数点前的数据
                    lines = [int(x.split(".")[0]) for x in lines]
                    line = dict(zip(self.TSV_INDEX, lines))
                    file_lines.append(line)
            tsv_file_datas[dir_name] = file_lines
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=f"get_tsv_data", msg=f"Error => {e}")
        return tsv_file_datas

    def get_csv_data(self, fp: str) -> dict:
        """
        解析csv 为0为空都直接转化成0
        :param fp:
        :return:dict
        """
        if not os.path.exists(fp):
            LogMessage(level=LOG_ERROR, module="get_tsv_data", msg="file is None")
            # return None
        dir_name = os.path.abspath(os.path.join(fp, "..")).split("\\")[-1]
        csv_file_datas = dict()
        try:
            with open(fp, "r", encoding="utf-8") as r:
                lines = [x for x in r.read().split("\n")[1:] if x != ""]
                csv_file_datas[dir_name] = [int(x) for x in lines if x is not None]
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=f"get_csv_data", msg=f"Error => {e}")
        return csv_file_datas

    def tsv_csv_data_fusion(self) -> list:
        """
        要把tsv，csv采集到的数据汇总制造一个数据结构后 调用画图模块制作多图合一
        :return:
        """
        full_datas = self.get_data_structure()
        all_files = list()
        for lines in full_datas:
            files = dict()
            file_name = list(lines.get("csv_data", None).keys())[0]
            csv_ = self.convert_csv_data(lines.get("csv_data", None).values())
            tsv_ = self.convert_tsv_data(lines.get("tsv_data", None).values())
            file_full_data = dict(list(csv_.items()) + list(tsv_.items()))
            files[file_name] = file_full_data
            all_files.append(files)
        return all_files

    def convert_tsv_data(self, tsv_data: dict) -> dict:
        """
        处理数据 需要做合并
        :param tsv_data:
        :return:
        """
        tsv_data = list(tsv_data)[0]
        tsv_map_data = dict()
        handle_count = list()
        private_bytes = list()
        virtual_bytes = list()
        working_set = list()
        working_set_private = list()
        processor_time = list()
        for line in tsv_data:
            pt_data = line.get(PROCESSOR_TIME, 0)
            processor_time.append(pt_data)
            hc_data = line.get(HANDLE_COUNT, 0)
            handle_count.append(hc_data)
            # bytes 转成 mb
            pb_data = line.get(PRIVATE_BYTES, 0) // 1024 // 1024
            private_bytes.append(pb_data)
            vb_data = line.get(VIRTUAL_BYTES, 0) // 1024 // 1024
            virtual_bytes.append(vb_data)
            ws_data = line.get(WORKING_SET, 0) // 1024 // 1024
            working_set.append(ws_data)
            wsp_data = line.get(WORKING_SET_PRIVATE, 0) // 1024 // 1024
            working_set_private.append(wsp_data)

        tsv_map_data[PROCESSOR_TIME] = processor_time
        tsv_map_data[HANDLE_COUNT] = handle_count
        tsv_map_data[PRIVATE_BYTES] = private_bytes
        tsv_map_data[VIRTUAL_BYTES] = virtual_bytes
        tsv_map_data[WORKING_SET] = working_set
        tsv_map_data[WORKING_SET_PRIVATE] = working_set_private
        return tsv_map_data

    def convert_csv_data(self, csv_data: dict) -> dict:
        """

        :param csv_data:
        :return:
        """
        fps_ = dict()
        fps_["fps"] = list(csv_data)[0]
        return fps_


FP = "C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\perf_data"
perf = PerfData(FP, "pc")
perf.tsv_csv_data_fusion()
