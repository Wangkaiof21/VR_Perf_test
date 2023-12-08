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
    # data.describe().round(2)  # 保留两位小数点
    # 指标汇总
    # data.aggregate([min, max, np.mean, np.std, np.median])
    # data.plot(figsize=(10, 12), subplots=True)  # 每列参数分离出来
    # plt.show()

    # 差异值
    # 计算每一天的差异值,后一天减去前一天的操作
    # print(data.diff().head())
    # print(data.diff().mean())

    # 增长率
    # 每一天的值没什么用,要求增长率(后一个值-前一个值)/前一个值
    # print(data.pct_change().head().round(3))
    # pct_change 增长率不该用折线图表示
    # data.pct_change().mean().plot(kind='bar', figsize=(10, 6))

    # 连续的增长率 使用log对数
    # res = np.log(data / data.shift(1))
    # res.head().round(3).plot(kind='bar', figsize=(10, 6))

    # 连续增长率的累加.cumsum(),apply这个方法要传进去一个函数，方法执行的时候，会对表格中每一个数据进行函数操作
    # rets = res.cumsum().apply(np.exp).plot(figsize=(10, 6))

    # 重采样
    # data.resample('1w').last().head()
    # data.resample('1m').last().head()
    # data.resample('1m',label='left').last().head() #不怎么用

    # 当前窗口最大最小平均序列值 基于窗口时间序列重采样
    # data.resample('1m').last().head()
    # data2 = data.copy().dropna()  # 建议复制一份,不能直接赋值,会告警,去掉缺失值
    # windows_num = 10
    # data2['min'] = data2['AAPL.O'].rolling(window=windows_num).min()
    # data2['max'] = data2['AAPL.O'].rolling(window=windows_num).max()
    # data2['mean'] = data2['AAPL.O'].rolling(window=windows_num).mean()
    # data2['std'] = data2['AAPL.O'].rolling(window=windows_num).std()

    # AAPL.O一只股票的短期平均+画图 金叉死叉
    # data2 = data.copy().dropna()
    # 短期平均5天
    # data2['min1'] = data2['AAPL.O'].rolling(window=5).mean()
    # 长期平均 20天一个交易月
    # data2['max2'] = data2['AAPL.O'].rolling(window=20).mean()
    # 算短期平均高于或者低于长期平均的时候设置一行标记为1,-1
    # data2['positions'] = np.where(data2['min1'] > data2['max2'], 1, -1)
    # 数据高度于不一致,设置个侧列 以达到明示的目的
    # data2[['AAPL.O', 'min1', 'max2', 'positions']].plot(figsize=(10, 6), secondary_y='positions')

    # 标普500指数SPX 恐慌指数VIX
    data3 = data.copy().dropna()[['.SPX', '.VIX']]
    # data3.plot(figsize=(10, 6), subplots=True)
    # 取两年的指数数据合成一张图
    data3.loc[:'2012-12-31'].plot(figsize=(12, 6), secondary_y='.VIX')

    # 散点图 直方图 和密度估计图 看趋势用的,spx,vix增加
    rets = np.log(data3 / data3.shift(1))
    pd.plotting.scatter_matrix(rets,
                               alpha=0.2,
                               diagonal='hits',
                               hist_kwds={'bins': 50},
                               figsize=(10, 6))
    # 直方图替换成曲线图,其实本质上直方图无限接近曲线图 bins是直方图需要的参数,曲线则不需要
    # pd.plotting.scatter_matrix(rets,
    #                            alpha=0.2,
    #                            diagonal='kde',
    #                            figsize=(10, 6))

    plt.show()


if __name__ == '__main__':
    file_name = 'data.csv'
    file_path = f'.//{file_name}'
    get_test_data(file_path)
