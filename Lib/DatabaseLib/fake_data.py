import random as rng
import string


def _gen_string(num: int) -> str:
    """
    根据传入num 生成num长度的种类字符串
    后期加入其他类型字符串
    :param num:
    :return:
    """
    return "".join(rng.choices(string.ascii_lowercase, k=num))


def gen_dummy_data(num):
    """
    根据传入num 生成多少组数据
    这里作为示例数据
    其实真正的情况里应该
    1、读取数据库里的相应的表 获取字段组成数据
    2、根据字段创造一个字典
    3、使用随机数模块往里面装填数据 返回出去
    :param num:
    :return:
    """
    cr_data = list()
    up_data = list()
    for index in range(num):
        cr_data.append({
            "string_var": _gen_string(10),
            "number_var": rng.randrange(1, 10000),
        })
        up_data.append({
            "string_var": _gen_string(10),
            "number_var": rng.randrange(1, 10000),
        })

    return cr_data, up_data
