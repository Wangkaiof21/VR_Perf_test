import pandas as pd
import numpy as np

if __name__ == '__main__':
    # s = pd.date_range("20221224", periods=10)
    # date_index = len(s)
    # index = "".join([str(x) for x in range(len(s))])
    # data_frame = pd.DataFrame(np.random.randn(date_index, date_index), index=s, columns=list(index))

    # data_frame2 = pd.DataFrame({
    #     "G": 1,
    #     "h": pd.Timestamp('20130102'),
    #     "3": pd.Series(1, index=list(range(7)), dtype='float32'),
    #     "A": np.array([3] * 7, dtype='int32'),
    #     "C": pd.Categorical(["test", "train", "test", "train","train", "test", "train"]),
    #     "E": 'foo',
    #     "G": 1,
    # })
    # # 打印头部数据
    # print(data_frame2.head(3))
    # # 打印尾部数据
    # print(data_frame2.tail(3))
    # # 可以快速查看数据的统计摘要
    # print(data_frame2.describe())
    index = pd.date_range('1/1/2000', periods=8)
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])
    df.columns = [x.lower() for x in df.columns]  # 把列名小写
    print(type(s.array))
