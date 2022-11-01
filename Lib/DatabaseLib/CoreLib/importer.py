import importlib
import importer
import typing


class ImportFromStringError(Exception):
    pass


def import_from_string(import_str: str = None) -> typing.Any:
    """
    动态引入
    检查模块是否可以被引入
    引入源文件自身
    第三方模块 import_from_github_com
    Python有一个编码规范就是EAPP：Easier to ask for forgiveness than permision。意思就是经常假设一些事情是存在的（例如，key在词典中），
    如果出错了，那么就捕获异常。你可以看 Python标准模块–import 文章中我们尝试引入模块，当它不存在时，我们就会捕获到ImportError。
    如果我们想检查并观察一个模块是否可以引入而不是仅仅是猜测，该如何去做？你可以使用importlib。
    导入的模块是否非要同一级别文件夹？
    :param import_str:
    :return:
    """
    module_str, _, attrs_str = import_str.partition(":")
    # 把特定字符串分解成三个值， partition()返回的是元组
    if not module_str or not attrs_str:
        message = ('Import string "{import_str}" must be in format "<module>:<attribute>".')
        raise ImportFromStringError(message.format(import_str=import_str))
    try:
        module = importlib.import_module(module_str)
        # 如果确定模块存在 则导入该模块 没有则报错对比模块名和输入名
    except ImportError as exc:
        if exc.name != module_str:
            raise exc from None
        message = 'Could not import module "{module_str}".'
        raise ImportFromStringError(message.format(module_str=module_str))
    instance = module
    try:
        for attr_str in attrs_str.split("."):
            instance = getattr(instance, attr_str)
            # getattr(obj, str)
            # 获取方法里面的属性的值 获取输入模块的方法里面的值
    except AttributeError as exc:
        message = 'Attribute "{attrs_str}" not found in module "{module_str}".'
        raise ImportFromStringError(
            message.format(attrs_str=attrs_str, module_str=module_str)
        )

    return instance

