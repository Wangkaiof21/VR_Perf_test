"""
封装一个matplotlib的类 能实现绘制折线，柱状，饼图
"""
import matplotlib
import matplotlib.pyplot as plt


class DrawMap:
    def __init__(self):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = "sans-serif"
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
