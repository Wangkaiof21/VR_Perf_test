import os
import sys
import time

FILE_PATH = "C:\\Users\\Administrator\\Desktop\\Perf_Test\\TestLog"
TEST_FLIE = "C:\\Users\\Administrator\\Desktop\\Perf_Test\\TestLog\\VRFrames1.csv"


class FPS:
    def __init__(self, test_log_path=None, test_file=None):
        self.test_log_path = test_log_path if isinstance(test_log_path, str) else print(f"The {test_log_path} not str")
        self.test_file = test_file if os.path.exists(test_file) else print(f"The path {test_log_path} not file!")

    def clean_old_test_log(self):
        """
        删除旧的log数据
        :return:
        """
        for root, dirs, files in os.walk(self.test_log_path):
            for file in files:
                if file.endswith(".csv"):
                    # print(f"{fp}\\{file}")
                    os.remove(f"{self.test_log_path}\\{file}")
                    return True
                else:
                    raise f"This {self.test_log_path} No files ending with .csv"

    def get_fps_data(self, index):
        """
        根据index获取所需要的列数据
        :param index:
        :return:
        """
        with open(self.test_file, "r", encoding="utf-8") as f:
            lines = f.read().split("\n")
            file_lines = list()
            for line in lines:
                print(line)
                file_lines.append(line)


def get_fps_list(fps_data):
    """
    把SystemTimeInSeconds处理成fps数据
    1/(n-(n-1)) 这里每一行都是一帧数据
    :param fps_data:
    :return:
    """
    fps_list = [x for x in fps_data if x != 0]
    fps_len = len(fps_list)
    # for _, value in enumerate(fps_list):
    #     print(_, value)
    fps_ = list()
    for index in range(len(fps_list)):
        if index == 0:
            fps_.append(1 // (fps_list[index] - 12295.981575))
        elif index > 0:
            fps_.append(1 // (fps_list[index] - (fps_list[index - 1])))
    print(fps_)


if __name__ == '__main__':
    fps = FPS(FILE_PATH, TEST_FLIE)
    fps.get_fps_data()
