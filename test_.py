import os

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

_array = np.arange(0, 100, 10)
print(np.where(_array >= 30))  # 返回符合要求的数组位置

_array2 = np.arange(0, 100, 2)
print(_array2.dtype)
print(_array2.astype(np.float32))  # 改变数组内的数据类型

# 数组运算
_array3 = np.array([[1, 2, 3], [4, 5, 6]])
row_list = np.sum(_array3, axis=0)  # 以行进行运算
print(row_list)
col_list = np.sum(_array3, axis=1)  # 以列进行运算
print(col_list)
# 同理min 和max方法也一样
print(np.min(_array3, axis=1))
print(np.max(_array3, axis=1))
print(np.argmin(_array3, axis=1))  # 求这列中最小值的位置
print(np.argmax(_array3, axis=1))  # 求这列中最大值的位置
print(np.mean(_array3, axis=1))  # 求这列中平均值
