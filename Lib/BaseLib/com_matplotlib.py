"""
封装一个matplotlib的类 能实现绘制折线，柱状，饼图
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class DrawMap:
    def __init__(self):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = "sans-serif"
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    def get_plot(self, x_list, y_list, title, save=True, grid_index=True, show=True) -> None:
        """
        接收特定数据绘制折线图 考虑到以后多重样本可能要做for循环绘制在一张图
        :param show: 是否展示
        :param grid_index: 网格线
        :param save:是否保存
        :param x_list:x轴内容 时间戳
        :param y_list:y轴内容 主数据
        :param title:
        :return:
        """
        index = np.arange(len(x_list))
        # 设置画板大小
        plt.figure(figsize=(10, 10))
        plt.title(f"{title}测试折线图")
        plt.xticks(index, x_list)
        if grid_index:
            plt.grid(grid_index, axis="y", linestyle="-", alpha=0.5)
        plt.plot(index, y_list)
        if show:
            plt.show()
        plt.close()
