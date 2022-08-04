import os
import sys


class CheckFilesSize:
    def __init__(self, fp):
        self.file_path = fp if isinstance(fp, str) else print("file address mismatch")
        self.size_dict = dict()

    def get_files_list(self):
        """
        通过绝对路径获取文件所有文件，文件大小组成字典
        :return:
        """
        flag = os.path.exists(self.file_path)
        mb_size = 1024 ** 2
        kb_size = 1024
        all_ = list()
        if flag:
            # 这里要计算出每个文件夹里面的文件数量、创建日期、大小（换算成kb？mb？ win里面小于1kb的文件默认展示成1kb）
            for root, dirs, files in os.walk(self.file_path):  # topdown=False
                file_collection = dict()
                file_package = list()
                size_num = 0
                for file in files:
                    file_msg = dict()
                    full_path = os.path.join(root, file)
                    file_size = round(os.path.getsize(full_path) / kb_size, 2)
                    file_msg[full_path] = file_size
                    # print(full_path, round(file_size / kb_size, 2))
                    file_package.append(file_msg)
                    size_num += file_size
                # print(root, round(size_num, 2), len(file_package), file_package)
                file_collection["dir"] = root
                file_collection["size"] = round(size_num, 2)
                file_collection["file_number"] = len(file_package)
                file_collection["file_list"] = file_package
                all_.append(file_collection)
        for line in all_:
            print(line)
            print("\n\n")


term = CheckFilesSize("C:\\Users\\Administrator\\Desktop\\test")
term.get_files_list()
