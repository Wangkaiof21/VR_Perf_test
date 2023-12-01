import os
import pandas as pd

# a = "KBE_RES_PATH = %KBE_ROOT%/kbe/res;%KBE_ROOT%/assets/;%KBE_ROOT%/assets/scripts;%KBE_ROOT%/assets/res/"
# b = a.replace("/", "\\")

# class Adb:
#     def __init__(self, fp):
#         self.test_path = fp
#     def test_cell(self):
#         self.index = self.test_path
#         print(f"强行赋值 - {self.index}")
#         return self.test_path
#
# adb = Adb("C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\TestLog>")
# print(adb.test_cell())
# import jsonpath
# import time
# import random
#
#
# class Adb_test:
#     def __init__(self):
#         self.nextMoveTime = int(time.time() + random.randint(5, 10))
#
#     def stop_(self):
#         if self.isMove:
#             # self.isMove = True
#             return "111111"
#         else:
#             # self.isMove = False
#             return "0"
#
# adb = Adb_test()
# adb.isMove = 1
# print(adb.stop_())

# def binSearch(arr, search_number):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = low + (high - low) // 2
#         if arr[mid] == search_number:
#             return mid
#         elif arr[mid] > search_number:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return "ERROR！"
#
#

# ret = binSearch(arr, 77)
#
# arr2 = [1, 123, 1999, 523, 42, 5, 4, 2, 324, 5, 2, 771, 77, 3, 4, 2, 4, 2,7758]
# print(arr2[:])

# class ObcTest:
#     def __init__(self, **args):
#         self._number = args
#
#     def get_num(self):
#         print(self._number["a"])
#         print(repr(self._number))
#
#
# A = ObcTest(a=123, b="test")
# A.get_num()

#
# def binary_search(test_list, item, rev=False):
#     """
#
#     :param test_list:
#     :param item: 被搜索的数
#     :param rev: 被搜索的数
#     :return:
#     """
#     test_list = list(set(test_list))
#     test_list.sort(reverse=False)
#     low = 0
#     high = len(test_list) - 1
#     while low <= high:
#         mid = (low + high) // 2  # 中间元素标记位
#         guess = test_list[mid]
#         print(f"guess --> {guess}", )
#         if guess == item:
#             return mid
#         if guess > item:  # 如果中间数大于目标数 则中心数减1
#             high = mid - 1
#         else:
#             low = mid + 1  # 如果中间数小于目标数 则中心数+1
#     return None


# if __name__ == '__main__':
#     list1 = [x for x in range(1, 99)]
#     binary_search(list1, 65)
# arr = [1, 123, 1999, 523, 42, 5, 4, 2, 324, 5, 2, 771, 77, 3, 4, 2, 4, 2, 7758]
# arr2 = list(set(arr))
# arr2.sort(reverse=True)
# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
#
#
# if __name__ == '__main__':
#     print(fact(9))

# def fact(index, arry_1):
#     """
#     数组阶乘
#     :param arry_1:
#     :param index:
#     :return:
#     """
#     if index == 0:
#         return arry_1[0]
#     else:
#         return arry_1[index] * fact(index, arry_1[index - 1])

# def quicksort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         print("pivot", pivot)
#         print("less", less)
#         print("greater", greater)
#         return quicksort(less) + [pivot] + quicksort(greater)
#
#
# if __name__ == '__main__':
#     arr = [1, 123, 1999, 523, 42, 5, 4, 2, 324, 5, 2, 771, 77, 3, 4, 2, 4, 2, 7758]
#     arr2 = list(set(arr))
#     # arr2.sort(reverse=True)
#     arr2.sort()
#     print(quicksort(arr))
#
# graph = dict()
# graph["you"] = ["alice", "bob", "claire"]
# graph["start"] = dict()
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
#
# graph["a"] = {}
# graph["a"]["fin"] = 1
#
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
#
# graph["fin"] = {}
#
# infinity = float("inf")
# costs = {"a": 6, "b": 2, "fin": infinity}
#
# parents = {"a": "start", "b": "start", "fin": None}
#
#
# def find_lowst_cost_node(costs):
#     low_costs = float("inf")
#     low_costs_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < low_costs and node not in processed:
#             low_costs = cost
#             low_costs_node = node
#     return low_costs_node


# from tkinter import Tk, Checkbutton, Frame, IntVar
#
#
# class Options:
#     def __init__(self, parent, name, selection=None, select_all=False):
#         self.parent = parent
#         self.name = name
#         self.selection = selection
#
#         self.variable = IntVar()
#         self.checkbutton = Checkbutton(self.parent, text=self.name,
#                                        variable=self.variable, command=self.check)
#
#         if selection is None:
#             self.checkbutton.pack(side='top')
#         elif select_all:
#             self.checkbutton.config(command=self.select_all)
#             self.checkbutton.pack()
#             for item in self.selection:
#                 item.checkbutton.pack(side='top')
#
#     def check(self):
#         state = self.variable.get()
#         if state == 1:
#             print(f'Selected: {self.name}')
#
#             if all([True if item.variable.get() == 1 else False for item in self.selection[:-1]]):
#                 self.selection[-1].checkbutton.select()
#
#         elif state == 0:
#             print(f'Deselected: {self.name}')
#
#             if self.selection[-1].variable.get() == 1:
#                 self.selection[-1].checkbutton.deselect()
#
#     def select_all(self):
#         state = self.variable.get()
#         if state == 1:
#             for item in self.selection[:-1]:
#                 item.checkbutton.deselect()
#                 item.checkbutton.invoke()
#         elif state == 0:
#             for item in self.selection[:-1]:
#                 item.checkbutton.select()
#                 item.checkbutton.invoke()
#
#
# selection = []
#
# root = Tk()
#
# option_frame = Frame(root)
# option_frame.pack(side='left', fill='y')
#
# for i in range(5):
#     selection.append(Options(option_frame, f'Option {i + 1}', selection))
# selection.append(Options(option_frame, 'Select All', selection, True))
#
# root.mainloop()

# i = int(input("test_data:"))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# result = 0
# for index in range(0, 6):
#     if i > arr[index]:
#         result += (i - arr[index]) * rat[index]  # 计算超过的部分奖金超过的部分 乘于 提成部分的值
#         i = arr[index]
# print(result)
# for x in range(1, 10):
#     for y in range(0, 10):
#         for z in range(0, 10):
#             d1 = x * 100 + y * 10 + z
#             d2 = pow(x, 3) + pow(y, 3) + pow(z, 3)
#             if d1 == d2:
#                 print(d1)
# for row in range(3):
#     for col in range(3):
#         Z[row][col] = X[row][col] +Y[row][col]
# sum_value = lambda x, y, z: x * y * z
# print(sum_value(169, 889, 395))

import numpy as np

# t_list = [1, 2, 3, 4, 3, 4, 13, 3124, 7]
# tang_array = np.array(t_list)
# print(tang_array.dtype)  # 内容字节
# print(np.shape(tang_array))  # 数组结构
# print(tang_array.size)  # 数量
# # print(tang_array.fill(0))  # 空数组填充零
# print(tang_array.ndim)  # 数组维度
#
# tang_array2 = np.array(
#     [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# )
# print(np.shape(tang_array2))
# tang_array3 = tang_array2.copy()  # 指向不同内存块
# tang3_array = np.arange(0, 100, 2)  # 从0开始到10，间隔是2

# mask = [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
# mask2 = np.array(mask, dtype=bool)  # 筛选结果变为布尔值，也可以为int 浮点

# random_array = np.random.rand(10)
# print(random_array >= 0.1)  # 判断数据中大于等于0.1的值

# _array = np.arange(0, 100, 10)
# print(np.where(_array >= 30))  # 返回符合要求的数组位置

# _array2 = np.arange(0, 100, 2)
# print(_array2.dtype)
# print(_array2.astype(np.float32))  # 改变数组内的数据类型

# 数组运算
# _array3 = np.array([[1, 2, 3], [4, 5, 6]])
# row_list = np.sum(_array3, axis=0)  # 以行进行运算
# print(row_list)
# col_list = np.sum(_array3, axis=1)  # 以列进行运算
# print(col_list)
# 同理min 和max方法也一样
# print(np.min(_array3, axis=1))
# print(np.max(_array3, axis=1))
# print(np.argmin(_array3, axis=1))  # 求这列中最小值的位置
# print(np.argmax(_array3, axis=1))  # 求这列中最大值的位置
# print(np.mean(_array3, axis=1))  # 求这列中平均值
# print(_array3.clip(2, 5))  # 即整个数组的值限制在指定值a_min,与a_max之间，对比a_min小的和比a_max大的值就重置为a_min,和a_max。
# print(_array3.round(decimals=1))  # 四舍五入几位数
# print(_array3.sort())  # 排序
# print(_array3.argsort())  # 排序且知道索引值
# print(np.linspace(0, 10, 9))  # 生成一个指定大小，指定数据区间的均匀分布序列 生成序列包含num个元素均匀分布在num的数量上

# value_list = np.linspace(0, 10, 13)
# insert_list = np.array([2.6, 3.5, 9.9])
# np.searchsorted(value_list, insert_list)  # 将数据搜索到并插入数组内，返回位置
# print(value_list)
#
# test_list = np.array([[100, 90, 95], [1, 2, 3], [999, 985, 9456]])
# index = np.lexsort([-1 * test_list[:, 0], test_list[:, -2]])  # 按照列来升序降序（-1，不输入值升序）排列
# []指定那一列 :指所有样本数字指那一列

# 改变array维度
# test_array = np.arange(10)
# print(test_array.reshape(2, 5)) # 把一维轴切割成两行五列
# 增加新轴
# test_array = test_array[:, np.newaxis]  # 在后面加一个轴
# test_array = test_array[np.newaxis, :]  # 在前面加一个轴
# test_array = test_array[:np.newaxis, np.newaxis]  # 在后面加两个轴
# print(test_array.shape)
# print(test_array)

# 剔除多余的轴
# squeeze_array = test_array.squeeze()
# print(squeeze_array.shape)
# 矩阵转阵列
# test_array2 = squeeze_array.reshape(2, 5)
# print(test_array2.transpose())
# print(test_array2.T)
# 链接数据
# a = np.arange(20, 30)
# b = np.arange(10)
# a = a.reshape(2, 5)
# b = b.reshape(2, 5)
# c = np.concatenate((a, b), axis=0)  # 等同于print(np.Ystack((a, b)))
# print(c.shape, c)  # 上下拼接
# d = np.concatenate((a, b), axis=1)  # 等同于print(np.Xstack((a, b)))
# print(d.shape, d)  # 横着拼接
#
# print(d.flatten())  # 突出数据拉长操作

# 构造数据
# print(np.zeros(3))  # 构建一个以0为基础的数组
# p_data = np.ones((3, 3), dtype=np.float32)  # 构建一个以1为基础的数组

# a = np.empty(6)
# a.fill(100)
# print(a)

# 构造维度和w1一摸一样以1为基础的数组
# w1 = np.zeros((3, 3))
# w2 = np.ones_like(w1)
# w3 = np.zeros_like(w1)
# print(w1, w2, w3, end="\n")

# 构造数据运算
# x = np.array([5, 1])
# y = np.array([3, 2])
# 乘法
# print(np.multiply(x, y))
# 内积计算 对位相乘且相加 有先后顺序
# print("dot = :", np.dot(x, y))
# print("dot = :", np.dot(y, x))
# 逻辑与或非
# x = np.arange(10)
# y = np.array([0, 10, 1, 0, 1, 10, 0, 1, 0, 1])
# print(np.logical_and(x, y))
# print(np.logical_or(x, y))
# print(np.logical_not(x, y))

# 随即模块
# s = np.random.rand(5, 6)  # 五行六列
# v = np.random.randint(99, size=(9, 9))  # 九行九列 整数随机0-99
# d = np.random.randint(0, 99, 10)  # 从0-9取10个随机数

# 高斯分布
# mu, sigma = 1, 100
# line = np.random.normal(mu, sigma, 10)
# np.set_printoptions(precision=2)  # 调整精度

# 洗牌操作
# nd_line = np.arange(10)
# np.random.shuffle(nd_line)  # 洗牌
# np.random.seed(100)  # 随机种子
# print(nd_line)


# np读数据
# 传统
# test_list = list()
# file_dir = "C:\\Users\\Administrator\\Desktop\\111\\VR_Perf_test\\tang_txt"
# with open(file_dir, 'r') as f:
#     for line in f.readline():
#         files = line.split()
#         cur_data = [float(x) for x in files]
#         test_list.append(cur_data)
# data = np.array(test_list)
# 等同于
# np.loadtxt(file_dir, delimiter=',', skiprows=1)# 意思是以逗号作为分割，不要第一行的表头
# txt_data = np.arange(10)
# txt_data.reshape(2, 5)
# txt_data = txt_data.reshape(2, 5)
# np.savetxt("txt.data", txt_data, fmt="%d", delimiter=",")
# 保存数据，fmt不已科学计数法保存

# pandas


# data = {"test_data": [1, 2, 3, 4, 3, 321, 54, 4321, 8, 5, 123, 5, 2123, 413],
#         "Name": [1324, 3, 4, 34, 234, "wei_lian", 14, 4, 32, 4, 324, 314, 32]}
# df = pd.DataFrame(data)

# df = df.set_index("Name")  # 指定顺序索引 可以set index之后直接查找人名所在的行 df['wei_lian']
#
# df.head()
# df.describe()  # 统计所有数值类型数据的基本特性
# df.loc[df['Sex'] == 'male', 'Age'].mean()
#      首先找到性别的为男性的乘客，然后找到样本数据为年龄的这一列 再.mean求平均操作

# groupby 统计
# 分型统计法，先把所有相关的元素获取然后进行操作，当我们直接使用统计值时，可以知道整体状况，比如所有人的年龄的平均值，但是比如我们想要知道：男性和女性的年龄分别是多少。这时我们就需要使用
# print(df.groupby('Sex').sum())
# print(df.groupby('Age').mean())  # 平均用的多
#
# print(df.groupby('Age').aggregate(np.mean))
# print(df.sum(axis=1))  # 求和操作可以指定行列和numpy
# print(df.sum(axis="Age"))  # 求和操作可以指定列明
# print(df.cov())  #
# print(df.corr())  # 求每一列的相关系数[1,-1]
# print(df["Age"].value_counts(ascending=True))  # 统计一列的不重复的数值指标 true为升序
# print(df["Age"].value_counts(ascending=True, bins=5))  # 统计一列的不重复的数值指标 true为升序 ,bins为划分区间
# print(df)
# data = [10, 11, 12]
# index = ['1', '2', '3']
# s = pd.Series(data=data, index=index)

# 数据表merge操作 将相同名字的列拼接 达到丰富行数据的操作
left_df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
right_df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                         'C': ['C0', 'C1', 'C2', 'C3'],
                         'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left_df, right_df, on='key')  # on=选择的列
print(res)
res2 = pd.merge(left_df, right_df, on=['key1', 'key2'], how='outer')  # how=假设列名字相同但数值有差异的表，可以用how他会把所有可能性列出以nan值填充
res3 = pd.merge(left_df, right_df, on=['key1', 'key2'], how='outer', indicator=True)  # 打开指示器，会把合并方法写出来 一般没啥用
