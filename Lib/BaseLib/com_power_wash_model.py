import os
import inspect
import numpy as np
import shutil
# from LogMessage import LogMessage, LOG_ERROR, LOG_RUN_INFO
# from com_matplotlib import DrawMap
from Lib.BaseLib.LogMessage import LogMessage, LOG_ERROR, LOG_RUN_INFO
from Lib.BaseLib.com_matplotlib import DrawMap

# from com_msg_center import MsgCenter
# MODULE_NAME = os.path.splitext(os.path.basename(__file__))[0]
# MsgCenter(MODULE_NAME,level=LOG_DEBUG)
np.set_printoptions(threshold=np.inf)


def get_func_name():
    return inspect.stack()[1][3]


class PowerWashPerfData:
    def __init__(self, base_dir, file_num, save_dir, save_index=None):
        self.index = file_num
        self.file_path = base_dir if os.path.exists(base_dir) else LogMessage(level=LOG_ERROR, module=get_func_name(),
                                                                              msg="data path dose not exist")
        self.save_path = save_dir if os.path.exists(save_dir) else LogMessage(level=LOG_ERROR, module=get_func_name(),
                                                                              msg="save path dose not exist")
        self.perf_data_path = os.path.join(self.file_path, str(self.index))
        self.save_index = save_index
        # TODO:关键字列表要从外层传入
        self.VR_INDEX = ['cpu_utilization_percentage', 'app_pss_MB', 'app_uss_MB', 'battery_level_percentage',
                         'average_frame_rate', 'Time Stamp', 'cpu_level', 'gpu_level']

    def get_file_data(self):
        """
        解析文件，把文件数据处理成合适的结构
        :return:
        """
        files_ = dict()
        try:
            for test_file in os.listdir(self.perf_data_path):
                test_file_dir = os.path.join(self.perf_data_path, test_file)
                for root, dirs, files in os.walk(test_file_dir):
                    if not os.listdir(root):
                        # 如果文件夹为空 则跳过
                        break
                    result = list()
                    case_name = os.path.abspath(os.path.join(test_file_dir)).split("\\")[-1]
                    for file_name in files:
                        file_full_dir = os.path.join(root, file_name)
                        data = self.get_vr_csv_data(file_full_dir, split_num_start=0, split_num_end=0)
                        result.append(data)
                    files_[case_name] = result
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"File error --> {e} !!!")
        try:
            # TODO:改成自动获取
            clean_save_path = f"{self.save_path}\\Quest2_image"
            if os.path.exists(clean_save_path):
                shutil.rmtree(clean_save_path)
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"File error --> {e} !!!")
        for case_name, val in files_.items():
            self.draw_vr_power_wash_map(str(case_name), val, save_path=self.save_path)
        return files_

    def get_vr_csv_data(self, fp: str, split_num_start: int, split_num_end: int, show=None) -> dict:
        """
        从绝对路径获取一体机数据，返回字典的形式
        这边要特殊处理 login文档的数据保留全的
        其他的要去掉头部login时间和尾部的退出程序时间
        :param fp:
        :param split_num_start:切割量的头
        :param split_num_end:切割量的尾
        :param show:调试用看单列筛洗数据
        :return:
        """
        if not os.path.exists(fp):
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg="file is None")
        # test_project_name = os.path.abspath(os.path.join(fp, "..")).split("\\")[-1]
        lines = list()
        result = dict()
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
        try:
            # test_num = random.randint(0, len(wash_lines))
            # if split_num_start > len(wash_lines[test_num]) or split_num_end > len(wash_lines[test_num]):
            #     LogMessage(level=LOG_ERROR, module=get_func_name(),
            #                msg=f"split_num {split_num_start}, split_num {split_num_end} out of the range")
            for line in wash_lines:
                key, val = line[0], [int(x) for x in line[1:]]
                if split_num_start and split_num_end:
                    result[key] = val[split_num_start:split_num_end]
                else:
                    result[key] = val
        except Exception as e:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"Error => {e}")
        show if show is None else LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"Data => {result}")

        return result

    def draw_vr_power_wash_map(self, case_name: str, perf_data: list, save_path: str) -> None:
        """
        一体机数据画图 可能有些问题 需要改进
        删除可能有点权限不足的问题 无法删除旧文件
        传入case_name，value
        case生成对应的包名，value做聚合数据 多折线存一图， 其中以最小列表基准长度为标准，生成聚合数据
        :param case_name: 测试用例名
        :param perf_data: list数据
        :param save_path: 保存地址 后面可能设置个默认的
        :return:
        """
        map_ = DrawMap()
        image_fp_ = save_path
        # 预留后期pico的文件路径
        image_save_path = f"{image_fp_}\\Quest2_image\\{case_name} image"
        # image_save_path = f"{image_fp_}\\PICO_image\\{case_name} image"
        os.makedirs(image_save_path)
        # 判断是否需要合并文件
        flag = len(perf_data)
        if flag == 1:
            for line in perf_data:
                file_time = [x for x in range(len(line.get(self.VR_INDEX[-1])))]
                del line[self.VR_INDEX[-1]]
                for key, value in line.items():
                    # print("dddd", key, value, len(file_time), len(value))
                    map_.get_plot(x_list=file_time, y_list=value, title=key, show=False, line_style='solid',
                                  x_label="time/s",
                                  y_label="fluctuation/s", x_lim=True, legend_index=(key,),
                                  x_ticks_list=[file_time[0], file_time[-1]], x_ticks_nums=[0, len(file_time)],
                                  save=True,
                                  path=f"{image_save_path}\\{key}.png")
        elif flag > 1:
            # 取一个标准值当作裁剪值，不然会报错
            min_index = list()
            for line in perf_data:
                min_index.append(line[self.VR_INDEX[-1]])
            index_ = len(min(min_index, key=len))
            # 重新封装 相同长度的数据
            new_list = list()
            for line in perf_data:
                dict_ = dict()
                for key, value in line.items():
                    dict_[key] = value[0:index_]
                new_list.append(dict_)
            # 把重新封装的数据按照相同的key合并成在一个list内 做三折线一体图，做三次测试保证严谨度
            dic = dict()
            for line in new_list:
                for k, v in line.items():
                    dic.setdefault(k, []).append(v)
            file_time = [x for x in range(len(dic.get(self.VR_INDEX[-1])[0]))]
            del dic[self.VR_INDEX[-1]]
            for key, val in dic.items():
                # print(key, val)
                map_.get_plots(x_list=val[0], y_list=val, title=key, show=False, line_style='solid',
                               x_label="time/s",
                               y_label="fluctuation/s", x_lim=True, legend_index=(key,),
                               x_ticks_list=[file_time[0], file_time[-1]], x_ticks_nums=[0, len(file_time)],
                               save=True,
                               path=f"{image_save_path}\\{key}.png")

            # lines = np.mat(np.array(a))
            # 求每一个数据的平均
            # z = list()
            # for line in lines:
            #     z.append(np.mean(line))
            # 求每所有数据的平均
            # print(np.sum(z) / len(lines))
        else:
            LogMessage(level=LOG_ERROR, module=get_func_name(), msg=f"Error!!")


# pw = PowerWashPerfData(base_dir="C:\\Users\\Administrator\Desktop\\vr_\\VR_Perf_test\\perf_data\\VR_PW_data",
#                        file_num=20221018,
#                        save_dir="C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\power_wash_image")
# pw.get_file_data()

# pw = PowerWashPerfData(base_dir="C:\\Users\\Administrator\Desktop\\vr_\\VR_Perf_test\\perf_data\\VR_PW_data",
#                        file_num=20221018,
#                        save_dir="C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\power_wash_image")

pw = PowerWashPerfData(base_dir="C:\\Users\\Administrator\Desktop\\vr_\\VR_Perf_test\\perf_data\\VR_level_data",
                       file_num=20230210,
                       save_dir="C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\power_wash_image")
pw.get_file_data()
