# import pandas as pd
#
# def get_data(fp):
#     csv_data = pd.read_csv(fp, error_bad_lines=False)
#     print(csv_data.to_string())
# if __name__ == '__main__':
#     csv_fp = "C:\\Users\\Administrator\\Desktop\\Perf_Test\\TestLog\\VRFrames1.csv"
#     get_data(csv_fp)
#


import numpy as np

arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]])
print(arr)
arr2 = arr.reshape(4,3)
print(arr2)
