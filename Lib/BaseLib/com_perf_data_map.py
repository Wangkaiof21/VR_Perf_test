"""
需求：
需要一个筛选出固定名字文档的模块，
需要一个读取csv，tsv文件的模块
需要一个数据处理模块
需要一个图形处理模块
"""

import os
from LogMessage import LogMessage, LOG_INFO, LOG_ERROR
from com_matplotlib import DrawMap

HANDLE_COUNT = 'Handle Count'
PRIVATE_BYTES = 'Private Bytes'
PROCESSOR_TIME = '% Processor Time'
VIRTUAL_BYTES = 'Virtual Bytes'
WORKING_SET = 'Working Set'
WORKING_SET_PRIVATE = 'Working Set - Private'
COMMITTED_BYTES = '% Committed Bytes In Use'
DATE_VALUE = 'time'
FPS = 'fps'
# 一体机vr
CPU_USED = 'cpu_utilization_percentage'
PSS_MEMORY = 'app_pss_MB'
USS_MEMORY = 'app_uss_MB'
BATTERY_PERCENT = 'battery_level_percentage'
FPS_ = 'average_frame_rate'
TIME_STAMP = 'Time Stamp'


class PerfData:
    def __init__(self, fp, index=None):
        """

        :param fp:
        :param index:
        """
        self.flag = index
        self.base_dir = fp if os.path.exists(fp) else LogMessage(level=LOG_ERROR, module="get_tsv_data",
                                                                 msg="path dose not exist")
        self.file_path = os.path.join(self.base_dir, "PC_Perf_data") if self.flag == "pc" else os.path.join(
            self.base_dir,
            "VR_Perf_data")
        self.TSV_INDEX = ["Processor Time", "Handle Count", "Private Bytes", "Virtual Bytes", "Working Set",
                          "Working Set - Private"]
        self.VR_INDEX = ['cpu_utilization_percentage', 'app_pss_MB', 'app_uss_MB', 'battery_level_percentage',
                         'average_frame_rate']

    def get_file_collector(self) -> list:
        """
        获取被测文件绝对路径列表
        这里逻辑不一样 pc端是有多种文件所以是列表套列表
        vr端是只有一个文件的 所以是单列表
        :return:
        """
        test_collector = list()
        if self.flag == "pc":
            try:
                for test_file in os.listdir(self.file_path):
                    test_file_dir = os.path.join(self.file_path, test_file)
                    files_ = list()
                    for root, dirs, files in os.walk(test_file_dir):
                        if not os.listdir(root):
                            # 如果文件夹为空 则跳过
                            break
                        for file_name in files:
                            if "DataCollector" in file_name or "fps" in file_name:
                                file_full_dir = os.path.join(root, file_name)
                                files_.append(file_full_dir)
                                # LogMessage(level=LOG_ERROR, module="get_file_path", msg=f"Error => {file_full_dir}")
                    test_collector.append(files_)
            except Exception as e:
                LogMessage(level=LOG_ERROR, module="get_file_path", msg=f"Error pc model=> {e}")
        elif self.flag == "vr":
            try:
                for test_file in os.listdir(self.file_path):
                    test_file_dir = os.path.join(self.file_path, test_file)
                    for root, dirs, files in os.walk(test_file_dir):
                        if not os.listdir(root):
                            # 如果文件夹为空 则跳过
                            break
                        elif os.listdir(root):
                            for file_name in files:
                                file_full_dir = os.path.join(root, file_name)
                                test_collector.append(file_full_dir)
            except Exception as e:
                LogMessage(level=LOG_ERROR, module="get_file_path", msg=f"Error vr model=> {e}")
        else:
            LogMessage(level=LOG_ERROR, module="get_file_path", msg=f"Error ！！！ ")
        return test_collector

    def get_data_structure(self) -> list:
        """
        分别从里面取出tsv，csv数据，整理成数据结构，不足的补0，缺失的置为0
        :return:
        """
        test_case_ = list()
        file_lines = self.get_file_collector()
        if self.flag == "pc":
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
        elif self.flag == "vr":
            for file_dir in file_lines:
                vr_csv_data = self.get_vr_csv_data(file_dir)
                test_case_.append(vr_csv_data)
        else:
            LogMessage(level=LOG_ERROR, module="get_data_structure", msg=f"Error ！！！ ")
        return test_case_

    # @staticmethod
    def get_vr_csv_data(self, fp: str) -> dict:
        """
        获取一体机数据，返回字典的形式
        这边要特殊处理 login文档的数据保留全的
        其他的要去掉头部login时间和尾部的退出程序时间
        :param fp:
        :return:
        """
        if not os.path.exists(fp):
            LogMessage(level=LOG_ERROR, module="get_vr_csv_data", msg="file is None")
        dir_name = os.path.abspath(os.path.join(fp, "..")).split("\\")[-1]
        file_datas = dict()
        try:
            lines = list()
            with open(fp, "r", encoding="utf-8") as r:
                vr_data_lines = r.read().split("\n")
                vr_index = vr_data_lines[0].split(",")
                for vr_data in vr_data_lines[1:]:
                    line = dict(zip(vr_index, [int(x) for x in vr_data.split(",")]))
                    lines.append(line)
            file_datas[dir_name] = lines
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=f"get_vr_csv_data", msg=f"Error => {e}")

        file = dict()
        for k, v in file_datas.items():
            fps = list()
            cpu = list()
            pss = list()
            uss = list()
            battery_ = list()
            date_ = list()
            clean_datas = dict()
            for line in self.VR_INDEX:
                clean_datas[line] = ""
            for line in v:
                date_.append(line.get(TIME_STAMP))
                fps.append(line.get(FPS_))
                pss.append(line.get(PSS_MEMORY))
                uss.append(line.get(USS_MEMORY))
                cpu.append(line.get(CPU_USED))
                battery_.append(line.get(BATTERY_PERCENT))
            clean_datas[FPS_] = fps
            clean_datas[PSS_MEMORY] = pss
            clean_datas[USS_MEMORY] = uss
            clean_datas[CPU_USED] = cpu
            clean_datas[BATTERY_PERCENT] = battery_
            clean_datas[TIME_STAMP] = date_
            file[k] = clean_datas
        for case_name, value_dict in file.items():
            # login数据不需要更改
            if case_name == "login":
                break
            else:
                file.get(case_name)[CPU_USED] = file.get(case_name).get(CPU_USED)[60:-20]
                file.get(case_name)[FPS_] = file.get(case_name).get(FPS_)[60:-20]
                file.get(case_name)[PSS_MEMORY] = file.get(case_name).get(PSS_MEMORY)[60:-20]
                file.get(case_name)[USS_MEMORY] = file.get(case_name).get(USS_MEMORY)[60:-20]
                file.get(case_name)[TIME_STAMP] = file.get(case_name).get(TIME_STAMP)[60:-20]
                file.get(case_name)[BATTERY_PERCENT] = file.get(case_name).get(BATTERY_PERCENT)[60:-20]
                # 原始数据 对比用
                # file.get(case_name)[CPU_USED] = file.get(case_name).get(CPU_USED)
                # file.get(case_name)[FPS_] = file.get(case_name).get(FPS_)
                # file.get(case_name)[PSS_MEMORY] = file.get(case_name).get(PSS_MEMORY)
                # file.get(case_name)[USS_MEMORY] = file.get(case_name).get(USS_MEMORY)
                # file.get(case_name)[TIME_STAMP] = file.get(case_name).get(TIME_STAMP)
                # file.get(case_name)[BATTERY_PERCENT] = file.get(case_name).get(BATTERY_PERCENT)
        return file

    @staticmethod
    def get_tsv_data(fp: str) -> dict:
        """
        获取tsv数据内容 新版功能数据
        tsv 数据长这样‘"1491"’，可能先需要strip()掉
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
                # 处理头部数据 列名先要分离出数据名 再把上级名字和带有电脑启用日期的数据去掉
                header_line = tsv_data[0].replace('"\t"', '').replace('"', '')
                header_line = header_line[16:].split("\\")
                header_line = [x for x in header_line if x != '']
                header_ = list()
                for index in range(len(header_line)):
                    if any([x.isdigit() for x in header_line[index]]) is False and header_line[index] \
                            != 'Process(HQVRMeeting)' and "Memory" not in header_line[index]:
                        header_.append(header_line[index])
                for lines in tsv_data[1:-1]:
                    # 切割转换的时候要把双引号去掉
                    lines = [x.strip('"') for x in lines.split("\t")]
                    # 保留时间戳
                    time_line = lines[0].split(" ")[-1].split(".")[0]
                    # 去掉时间戳列 和把空的数字用0替换
                    lines = ['0.00' if x == ' ' else x for x in lines[1:]]
                    # 要保留int类型数据，要保留小数点前的数据
                    lines = [int(x.split(".")[0]) for x in lines]
                    line = dict(zip(header_, lines))
                    line["time"] = time_line
                    file_lines.append(line)
                tsv_file_datas[dir_name] = file_lines
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=f"get_tsv_data", msg=f"Error => {e}")
        return tsv_file_datas

    @staticmethod
    def get_csv_data(fp: str) -> dict:
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

    @staticmethod
    def convert_tsv_data(tsv_data: dict) -> dict:
        """
        处理tsv数据 需要做合并
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
        committed_bytes = list()
        processor_time = list()
        time_list = list()
        for line in tsv_data:
            pt_data = line.get(PROCESSOR_TIME, 0)
            processor_time.append(pt_data)
            hc_data = line.get(HANDLE_COUNT, 0)
            handle_count.append(hc_data)
            memory_data = line.get(COMMITTED_BYTES, 0)
            committed_bytes.append(memory_data)
            date_ = line.get(DATE_VALUE, 0)
            time_list.append(date_)
            # 私有内存因为是bytes 转成 mb
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
        tsv_map_data[COMMITTED_BYTES] = committed_bytes
        tsv_map_data[DATE_VALUE] = time_list
        return tsv_map_data

    @staticmethod
    def convert_csv_data(csv_data: dict) -> dict:
        """
        把fps文件里的数据处理一下
        :param csv_data:
        :return:
        """
        fps_ = dict()
        fps_["fps"] = list(csv_data)[0]
        return fps_

    def draw_map(self):
        """
        获得数据 在每一个原始文件的目录下新建一个文件夹或者直接以散装图片的方式塞进去
        pc数据是分离的 得组合后在处理
        :return:
        """
        datas = self.tsv_csv_data_fusion()
        map_ = DrawMap()
        image_fp_ = "C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\perf_image"
        for files in datas:
            (key, value), = files.items()
            image_save_path = f"{image_fp_}\\PC_image\\{key} image"
            if os.path.exists(image_save_path):
                os.remove(image_save_path)
                os.makedirs(image_save_path)
            else:
                os.makedirs(image_save_path)
            fps_data = value.get(FPS)
            x_ticks = [x for x in range(len(fps_data))]
            fps_name = f"{key} {FPS}.png"
            map_.get_plot(x_list=fps_data, y_list=fps_data, title=FPS, show=False, line_style='solid',
                          x_label="second/s",
                          y_label="fps/s", legend_index=(FPS,), save=True, path=f"{image_save_path}\\{fps_name}",
                          x_ticks_list=[x_ticks[0], x_ticks[-1]], x_ticks_nums=[0, len(x_ticks)])
            # print(f"{image_save_path}\\{fps_name}")
            del value[FPS]
            file_time = value[DATE_VALUE]
            del value[DATE_VALUE]
            for name, values in value.items():
                # print(f"{image_save_path}\\{name}.png")
                map_.get_plot(x_list=file_time, y_list=values, title=name, show=False, line_style='solid',
                              x_label="time/s",
                              y_label="fluctuation/s", x_lim=True, legend_index=(name,),
                              x_ticks_list=[file_time[0], file_time[-1]], x_ticks_nums=[0, len(file_time)], save=True,
                              path=f"{image_save_path}\\{name}.png")

    def draw_vr_map(self):
        """
        一体机数据画图 可能有些问题 需要改进
        可能会有文件权限不足的问题 无法删除旧文件
        :return:
        """
        datas = self.get_data_structure()
        map_ = DrawMap()
        image_fp_ = "C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\perf_image"
        # image_fp_ = "D:\\"
        for lines in datas:
            for case_name, values in lines.items():
                image_save_path = f"{image_fp_}\\VR_image\\{case_name} image"
                if os.path.exists(image_save_path):
                    # 删除可能有点权限问题
                    os.remove(image_save_path)
                    os.makedirs(image_save_path)
                else:
                    os.makedirs(image_save_path)
                file_time = [x for x in range(len(values[TIME_STAMP]))]
                del values[TIME_STAMP]
                # print(values)
                for key, value in values.items():
                    # print("dddd", key, value, len(file_time), len(value))
                    map_.get_plot(x_list=file_time, y_list=value, title=key, show=False, line_style='solid',
                                  x_label="time/s",
                                  y_label="fluctuation/s", x_lim=True, legend_index=(key,),
                                  x_ticks_list=[file_time[0], file_time[-1]], x_ticks_nums=[0, len(file_time)],
                                  save=True,
                                  path=f"{image_save_path}\\{key}.png")


FP = "C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\perf_data"
# perf = PerfData(FP, "pc")
# perf.draw_map()
perf = PerfData(FP, "vr")
perf.draw_vr_map()
