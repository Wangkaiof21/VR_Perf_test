import asyncio
import contextlib
import functools
import inspect
import logging
from Lib.BaseLib.LogMessage import LogMessage, LOG_RUN_INFO, LOG_ERROR, LOG_WARN
import typing
from contextvars import ContextVar
from types import TracebackType
from urllib.parse import SplitResult, parse_qsl, unquote, urlsplit

from sqlalchemy import text
from sqlalchemy.sql import ClauseElement

from Lib.DatabaseLib.CoreLib.importer import import_from_string
from Lib.DatabaseLib.CoreLib.interfaces import DatabaseBackend, Record

try:  # pragma: no cover
    import click

    # Extra log info for optional coloured terminal outputs.
    LOG_EXTRA = {
        "color_message": "Query: " + click.style("%s", bold=True) + " Args: %s"
    }
    CONNECT_EXTRA = {
        "color_message": "Connected to database " + click.style("%s", bold=True)
    }
    DISCONNECT_EXTRA = {
        "color_message": "Disconnected from database " + click.style("%s", bold=True)
    }
except ImportError:  # pragma: no cover
    LOG_EXTRA = {}
    CONNECT_EXTRA = {}
    DISCONNECT_EXTRA = {}


def get_func_name():
    return inspect.stack()[1][3]


class Database:
    SUPPORTED_BACKENDS = {
        "postgresql": "databases.backends.postgres:PostgresBackend",
        "postgresql+aiopg": "databases.backends.aiopg:AiopgBackend",
        "postgres": "databases.backends.postgres:PostgresBackend",
        "mysql": "databases.backends.mysql:MySQLBackend",
        "mysql+asyncmy": "databases.backends.asyncmy:AsyncMyBackend",
        "sqlite": "databases.backends.sqlite:SQLiteBackend",
    }

    # typing.Union[str, "DatabaseURL"]
    #
    # 传入类名 返回类的类型
    def __init__(self, url: typing.Union[str, "DatabaseURL"], *, force_rollback: bool = False, **options: typing.Any):
        # Union[str, "DatabaseURL"]
        # 代表联合类型，这个参数里可以传入两种以上类型，DatabaseURL方法返回类型的字符串或str的数据库地址。
        # 放在类的结果后面表示，返回两种、两种以上类型

        self.url = DatabaseURL(url)
        self.options = options
        LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"url => {self.url}")
        LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg=f"option => {self.options}")
        self.is_connected = False
        self._force_rollback = force_rollback

        backend_str = self._get_backend()
        backend_cls = import_from_string(backend_str)
        assert issubclass(backend_cls, DatabaseBackend)
        self._backend = backend_cls(self.url, **self.options)
        # issubclass函数主要用于判断一个对象是否为另外一个对象的子类
        self.connection_context = ContextVar("connection_context")  # type: ContextVar
        self._global_connection = None  # type: typing.Optional[Connection]
        self._global_transaction = None  # type: typing.Optional[Transaction]

    async def connect(self) -> None:
        """
        Establish the connection pool.
        建立连接池
        :return:
        """
        if self.is_connected:
            LogMessage(level=LOG_RUN_INFO, module=get_func_name(), msg="Already connected, skipping connection")
            return None
        await self._backend.connect()

    def _get_backend(self) -> str:
        """
        返回从字典get到的数据库类型
        没有则返回
        :return:
        """
        print(self.SUPPORTED_BACKENDS.get(self.url.scheme, self.SUPPORTED_BACKENDS[self.url.dialect]))
        return self.SUPPORTED_BACKENDS.get(self.url.scheme, self.SUPPORTED_BACKENDS[self.url.dialect])


class DatabaseURL:
    def __init__(self, url: typing.Union[str, "Database"]):
        """
        第二个理解是第二次调方法的时候不需要传值，上一次的值会留下来提高性能？
        :param url:
        """
        if isinstance(url, DatabaseURL):
            self._url: str = url._url
        elif isinstance(url, str):
            self._url = url
        else:
            raise TypeError(
                f"Invalid type for DatabaseURL. Expected str or DatabaseURL, got {type(url)}"
            )

    @property
    def components(self) -> SplitResult:
        """
        property 可以直接对属性赋值，外层直接调用，比类自带的get_name,set_name方法更好用
        直接返回被装饰方法的结果不需要实例化

        p1 = DatabaseURL('localhost//:16086')
        p1.components='a'
        print(p1.components)
        ---------------result-------------------
        'a'

        组件
        :return:
        """
        if not hasattr(self, "_components"):
            # hasattr() 判断方法是否包含对应属性
            self._components = urlsplit(self._url)
            # 这边会按照urlsplit的方案分割数据库地址
        return self._components

    @property
    def scheme(self) -> str:
        """
        返回数据库类型
        :return:
        """
        return self.components.scheme

    @property
    def dialect(self) -> str:
        """
        返回数据库类型
        :return:
        """
        return self.components.scheme.split("+")[0]

    @property
    def driver(self) -> str:
        if "+" not in self.components.scheme:
            return ""
        return self.components.scheme.split("+", 1)[1]

    @property
    def userinfo(self) -> typing.Optional[bytes]:
        """
        返回bytes类型的用户名用户密码，没有则返回空
        :return:
        """
        if self.components.username:
            info = self.components.username
            if self.components.password:
                info += ":" + self.components.password
            # print(repr(info.encode("utf-8")))
            return info.encode("utf-8")
        return None

    @property
    def username(self) -> typing.Optional[str]:
        """
        子方法 单独返回用户名
        :return:
        """
        if self.components.username is None:
            return None
        return unquote(self.components.username)

    @property
    def password(self) -> typing.Optional[str]:
        """
        子方法 单独返回用户密码
        :return:
        """
        if self.components.password is None:
            return None
        return unquote(self.components.password)

    @property
    def hostname(self) -> typing.Optional[str]:
        """
        返回地址
        :return:
        """
        return (
                self.components.hostname
                or self.options.get("host")
                or self.options.get("unix_sock")
        )

    @property
    def options(self) -> dict:
        """
        返回数据库地址选项，
        parse_qsl 把选项部分拆解为列表包元组[(),()]
        :return:
        """
        if not hasattr(self, "_options"):
            self._options = dict(parse_qsl(self.components.query))
        return self._options

    @property
    def port(self) -> typing.Optional[int]:
        """
        端口
        :return:
        """
        return self.components.port

    @property
    def netloc(self) -> typing.Optional[str]:
        """
        网络地址
        :return:
        """
        return self.components.netloc

    @property
    def database(self) -> str:
        """
        获取数据库名
        unquote 是处理成url想要的数据
        :return:
        """
        path = self.components.path
        if path.startswith("/"):
            path = path[1:]
        return unquote(path)

    # def url_replace(self, **kwargs: typing.Any) -> typing.Any:
    def url_replace(self, **kwargs: typing.Any) -> "DatabaseURL":
        """
        **kwargs的情况下，入参值的名字可以随便定义
        把明文信息转换成*********
        進來的kwargs是個字典
        :param kwargs:
        :return:
        """

        if (
                "username" in kwargs
                or "password" in kwargs
                or "hostname" in kwargs
                or "port" in kwargs
        ):
            hostname = kwargs.pop("hostname", self.hostname)
            port = kwargs.pop("port", self.port)
            username = kwargs.pop("username", self.components.username)
            password = kwargs.pop("password", self.components.password)
            netloc = hostname
            if port is not None:
                netloc += f":{port}"
            if username is not None:
                userpass = username
                if password is not None:
                    userpass += f":{password}"
                netloc = f"{userpass}@{netloc}"
            kwargs['netloc'] = netloc
        if "database" in kwargs:
            kwargs["path"] = "/" + kwargs.pop("database")
        if "dialect" in kwargs or "driver" in kwargs:
            dialect = kwargs.pop("dialect", self.dialect)
            driver = kwargs.pop("driver", self.driver)
            kwargs["scheme"] = f"{dialect}+{driver}" if driver else dialect
        if not kwargs.get("netloc", self.netloc):
            kwargs["netloc"] = _EmptyNetloc()
        components = self.components._replace(**kwargs)
        return self.__class__(components.geturl())

    @property
    def obscure_password(self) -> str:
        if self.password:
            return self.url_replace(password="********")._url
        return self._url

    def __str__(self) -> str:
        return self._url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.obscure_password)})"

    def __eq__(self, other: typing.Any) -> bool:
        """
        这个类传创建的对象在判断的时候全都为相等
        默认调用python的is方法
        :param other:
        :return:
        """
        return str(self) == str(other)


class _EmptyNetloc(str):
    """
    这个类传创建的对象在判断的时候全都为真
    在其他方法判断是否存在的总是返回真
    """

    def __bool__(self) -> bool:
        return True


test_url = "mysql://192.168.1.1:3306/ry?useUnicode=&useJDBCCompliantTimezoneShift=&useLegacyDatetimeCode=&serverTimezone=PRC&characterEncoding=UTF8"
# a1 = DatabaseURL(test_url)

a2 = Database(test_url)
