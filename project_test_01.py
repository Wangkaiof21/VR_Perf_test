import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_test_data(fp):
    """

    :param fp:
    :return: None
    """
    data = pd.read_csv(fp, index_col=0, parse_dates=True)
    # print(data.info())  # 看样本量
    data.describe().round(2)  # 保留两位小数点
    # 指标汇总
    # data.aggregate([min, max, np.mean, np.std, np.median])
    # data.plot(figsize=(10, 12), subplots=True)  # 每列参数分离出来
    # plt.show()

    # 计算每一天的差异值,后一天减去前一天的操作
    # print(data.diff().head())
    # print(data.diff().mean())

    # 每一天的值没什么用,要求增长率(后一个值-前一个值)/前一个值
    # print(data.pct_change().head().round(3))
    # 增长率不该用折线图表示
    # data.pct_change().mean().plot(kind='bar', figsize=(10, 6))
    # 连续的增长率 使用log对数
    res = np.log(data / data.shift(1))
    #  
    res.head().round(3).plot(kind='bar', figsize=(10, 6))
    # data.pct_change().mean().plot(kind='bar', figsize=(10, 6))
    plt.show()


if __name__ == '__main__':
    file_name = 'data.csv'
    file_path = f'.//{file_name}'
    get_test_data(file_path)
