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

def binSearch(arr, search_number):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == search_number:
            return mid
        elif arr[mid] > search_number:
            high = mid - 1
        else:
            low = mid + 1
    return "ERROR！"


arr = [1, 123, 1999, 523, 42, 5, 4, 2, 324, 5, 2, 771, 77, 3, 4, 2, 4, 2,7758]
arr = list(set(arr))
ret = binSearch(arr, 77)

arr2 = [1, 123, 1999, 523, 42, 5, 4, 2, 324, 5, 2, 771, 77, 3, 4, 2, 4, 2,7758]
print(arr2[:])

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
