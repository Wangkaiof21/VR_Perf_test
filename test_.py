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

os.mkdir("C:\\Users\\Administrator\\Desktop\\vr_\\VR_Perf_test\\power_wash_image")
data = [{'app_pss_MB': [285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285, 285,
                        1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148, 1148,
                        1148, 1148, 1148, 1148, 1151, 1151, 1151, 1151, 1151, 1151, 1151, 1151, 1151, 1151, 1151, 1151,
                        1151, 1151, 1151, 1151, 1151, 1151, 1151, 1151, 1153, 1153, 1153, 1153, 1153, 1153, 1153, 1153,
                        1153, 1153, 1153, 1153, 1153, 1153, 1153, 1153, 1153, 1153, 1153, 1153, 1154, 1154, 1154, 1154,
                        1154, 1154, 1154, 1154, 1154, 1154, 1154, 1154, 1154, 1154, 1154, 1154, 1154, 1236, 1236, 1236,
                        1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236, 1236,
                        1236, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238,
                        1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238,
                        1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1238, 1239, 1239, 1239, 1239, 1239, 1239, 1239,
                        1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239,
                        1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239,
                        1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239, 1239,
                        1239, 1239, 1239, 1239, 1239, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241,
                        1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1240, 1240, 1240, 1240, 1240, 1240, 1240,
                        1240, 1240, 1240, 1240, 1240, 1240, 1240, 1240, 1240, 1240, 1240, 1240, 1240, 1241, 1241, 1241,
                        1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241,
                        1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241,
                        1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241,
                        1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241, 1241]}, {
            'battery_level_percentage': [66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
                                         66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67,
                                         67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67,
                                         67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67,
                                         67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67,
                                         67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67,
                                         67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68,
                                         68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68]}, {
            'average_frame_rate': [73, 72, 72, 73, 17, 17, 6, 58, 58, 58, 58, 58, 58, 49, 66, 72, 72, 72, 72, 72, 73,
                                   72, 72, 73, 72, 73, 72, 73, 73, 73, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73,
                                   73, 72, 73, 73, 73, 73, 73, 73, 73, 73, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73,
                                   73, 73, 73, 73, 73, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 70, 73, 73,
                                   73, 73, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 62, 67, 63, 70, 69, 70, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 70, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 71, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 69, 72,
                                   72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 68, 67, 70, 55,
                                   48, 48]}, {
            'cpu_utilization_percentage': [13, 9, 9, 55, 80, 80, 80, 19, 19, 19, 19, 19, 94, 19, 14, 27, 15, 28, 19, 21,
                                           25, 23, 28, 27, 23, 25, 28, 27, 31, 31, 23, 27, 30, 34, 25, 33, 34, 23, 25,
                                           28, 27, 23, 34, 33, 23, 21, 23, 23, 31, 23, 23, 23, 23, 33, 23, 28, 23, 23,
                                           28, 23, 25, 19, 30, 19, 27, 30, 23, 19, 19, 25, 23, 21, 19, 25, 31, 28, 30,
                                           27, 23, 31, 23, 27, 30, 30, 21, 28, 30, 30, 31, 27, 28, 30, 27, 33, 33, 33,
                                           27, 19, 19, 19, 31, 33, 22, 23, 19, 19, 19, 26, 14, 26, 18, 19, 27, 19, 19,
                                           27, 23, 19, 28, 23, 22, 27, 23, 19, 22, 19, 19, 22, 14, 19, 22, 22, 23, 26,
                                           19, 19, 18, 27, 22, 19, 19, 19, 21, 22, 19, 23, 27, 22, 27, 27, 18, 23, 22,
                                           19, 19, 19, 23, 22, 22, 19, 26, 22, 22, 19, 18, 22, 26, 21, 26, 14, 19, 26,
                                           22, 23, 26, 26, 21, 23, 19, 26, 22, 22, 19, 23, 26, 22, 26, 21, 22, 22, 26,
                                           22, 22, 15, 19, 19, 21, 22, 21, 21, 26, 23, 30, 19, 30, 19, 26, 19, 25, 23,
                                           18, 22, 22, 22, 19, 22, 26, 26, 19, 27, 22, 30, 26, 22, 27, 15, 29, 27, 26,
                                           26, 22, 22, 19, 30, 22, 19, 19, 22, 26, 14, 11, 15, 29, 26, 22, 19, 14, 30,
                                           19, 27, 23, 19, 19, 19, 27, 19, 26, 22, 29, 19, 19, 26, 22, 22, 19, 14, 26,
                                           27, 19, 23, 29, 26, 30, 23, 30, 19, 23, 19, 27, 26, 13, 22, 19, 19, 19, 25,
                                           29, 30, 30, 19, 22, 25, 23, 19, 22, 19, 25, 31, 22, 22, 27, 22, 22, 19, 19,
                                           19, 22, 27, 23, 23, 26, 23, 27, 22, 18, 14, 14]}, {
            'app_uss_MB': [277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277, 277,
                           277, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132, 1132,
                           1132, 1132, 1132, 1132, 1132, 1132, 1136, 1136, 1136, 1136, 1136, 1136, 1136, 1136, 1136,
                           1136, 1136, 1136, 1136, 1136, 1136, 1136, 1136, 1136, 1136, 1136, 1137, 1137, 1137, 1137,
                           1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137, 1137,
                           1137, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138, 1138,
                           1138, 1138, 1138, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220,
                           1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1221, 1221, 1221, 1221, 1221, 1221, 1221,
                           1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221,
                           1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221, 1221,
                           1221, 1221, 1221, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222,
                           1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222,
                           1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1222, 1223, 1223,
                           1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223, 1223,
                           1223, 1223, 1223, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224,
                           1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224,
                           1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1224, 1225, 1225,
                           1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225,
                           1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225,
                           1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225,
                           1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225, 1225]}]
