"""
封装一个matplotlib的类 能实现绘制折线，柱状，饼图
"""
import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class DrawMap:
    def __init__(self):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = "sans-serif"
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    def get_plot(self, x_list, y_list, title, x_label="x轴", y_label="y轴", save=True, grid_index=True, show=True,
                 line_style=None, path=None, line_color=None, x_lim=False, legend_index=None, x_ticks_nums=None,
                 x_ticks_list=None) -> None:
        """
        接收特定数据绘制折线图 考虑到以后多重样本可能要做for循环绘制在一张图
        :param x_ticks_list: x轴刻度专用list
        :param x_ticks_nums: x轴刻度数量
        :param legend_index:图例
        :param x_lim: 控制x轴间隔数 输入列表的最大最小值
        :param line_color: 线条颜色
        :param y_label:刻度属性名字
        :param x_label:刻度属性名字
        :param path: 存储路径
        :param line_style: 线条形态 => '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
        :param show: 是否展示
        :param grid_index: 网格线
        :param save:是否保存
        :param x_list:x轴内容 时间戳
        :param y_list:y轴内容 主数据
        :param title:图片名字
        :return:
        """

        # 设置画板大小
        fig, ax = plt.subplots(figsize=(16, 12))
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(f"{title}测试折线图")
        """
        x刻度和x生成轴的是不一样的 刻度需要数量和固定内容 生成轴的则需要列表推导式 
        比如说这边nums是输入x刻度要显示的数量 ，x刻度list里面就必须要有多少个相对应的值
        nums = [0,999] x_list=[0,1,2,3,......,999]
        """
        x_index = np.arange(len(x_list))
        if x_ticks_nums and x_ticks_list:
            # print(x_ticks_nums, x_ticks_list)
            plt.xticks(x_ticks_nums, x_ticks_list)
        else:
            plt.xticks(x_index, x_list)
        # print(repr(x_index))
        if grid_index:
            plt.grid(grid_index, axis="y", linestyle=line_style, alpha=0.5)
        plt.plot(x_index, y_list, color=line_color, lw=5, marker="o", markersize=4.5,
                 markerfacecolor="red", markeredgewidth=2, markeredgecolor="grey")
        plt.legend(legend_index, )
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        if show:
            plt.show()
        if save and path:
            # if not os.path.exists(path):
            #     os.mkdir(path)
            # else:
            plt.savefig(path)
        plt.close()

    def get_plots(self, x_list, y_list, title, x_label="x轴", y_label="y轴", save=True, grid_index=True, show=True,
                  line_style=None, path=None, line_color=None, x_lim=False, legend_index=None, x_ticks_nums=None,
                  x_ticks_list=None) -> None:
        """
        多数组，后期合并到get_plot 判断多数组
        接收特定数据绘制折线图 考虑到以后多重样本可能要做for循环绘制在一张图
        :param x_ticks_list: x轴刻度专用list
        :param x_ticks_nums: x轴刻度数量
        :param legend_index:图例
        :param x_lim: 控制x轴间隔数 输入列表的最大最小值
        :param line_color: 线条颜色
        :param y_label:刻度属性名字
        :param x_label:刻度属性名字
        :param path: 存储路径
        :param line_style: 线条形态 => '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
        :param show: 是否展示
        :param grid_index: 网格线
        :param save:是否保存
        :param x_list:x轴内容 时间戳
        :param y_list:y轴内容 主数据
        :param title:图片名字
        :return:
        """

        # 设置画板大小
        fig, ax = plt.subplots(figsize=(16, 12))
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(f"{title}测试折线图")
        """
        x刻度和x生成轴的是不一样的 刻度需要数量和固定内容 生成轴的则需要列表推导式 
        比如说这边nums是输入x刻度要显示的数量 ，x刻度list里面就必须要有多少个相对应的值
        nums = [0,999] x_list=[0,1,2,3,......,999]
        """
        x_index = np.arange(len(x_list))
        if x_ticks_nums and x_ticks_list:
            # print(x_ticks_nums, x_ticks_list)
            plt.xticks(x_ticks_nums, x_ticks_list)
        else:
            plt.xticks(x_index, x_list)
        if grid_index:
            plt.grid(grid_index, axis="y", linestyle=line_style, alpha=0.5)
        for index in range(len(y_list)):
            plt.plot(x_index, y_list[index], color=line_color, lw=5, marker="o", markersize=4.5,
                     markerfacecolor="red", markeredgewidth=2, markeredgecolor="grey")
            # plt.legend(f"{legend_index}_{index}", )
        # for line in y_list:
        #     plt.plot(x_index, line, color=line_color, lw=5, marker="o", markersize=4.5,
        #              markerfacecolor="red", markeredgewidth=2, markeredgecolor="grey")
        # plt.legend(legend_index, )
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        if show:
            plt.show()
        if save and path:
            # if not os.path.exists(path):
            #     os.mkdir(path)
            # else:
            plt.savefig(path)
        plt.close()


# daw = DrawMap()
#
# name = "app_pss_MB"
# data = [
#     [276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 276, 1131, 1131, 1131,
#      1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1131, 1133, 1133,
#      1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 1133, 277,
#      277, 277],
#     [285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 1147, 1147, 1147,
#      1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1149, 1149,
#      1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1149, 1150,
#      1150, 1150],
#     [285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 1145, 1145, 1145,
#      1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1145, 1147, 1147,
#      1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1147, 1148,
#      1148, 1148]]
# file_time = [x for x in range(len(data[0]))]
# daw.get_plots(x_list=data[0], y_list=data, title=name, show=True, line_style='solid',
#               x_label="time/s",
#               y_label="fluctuation/s", x_lim=True, legend_index=(name,),
#               x_ticks_list=[file_time[0], file_time[-1]], x_ticks_nums=[0, len(file_time)],
#               save=False,
#               path=f"C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\power_wash_image\\{name}.png")
