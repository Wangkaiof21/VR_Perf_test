import asyncio
import contextlib
import functools
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

logger = logging.getLogger("databases")


class Database:
    SUPPORTED_BACKENDS = {
        "postgresql": "databases.backends.postgres:PostgresBackend",
        "postgresql+aiopg": "databases.backends.aiopg:AiopgBackend",
        "postgres": "databases.backends.postgres:PostgresBackend",
        "mysql": "databases.backends.mysql:MySQLBackend",
        "mysql+asyncmy": "databases.backends.asyncmy:AsyncMyBackend",
        "sqlite": "databases.backends.sqlite:SQLiteBackend",
    }

    def __init__(self, url: typing.Union[str, "DatabaseURL"], *, force_rollback: bool = False, **options: typing.Any):
        # Union[str, "DatabaseURL"] 意思是可以传两种类型的值，Union的字符串或Union的数据库地址
        self.url = DatabaseURL(url)
        self.options = options
        self.is_connected = False
        self._force_rollback = force_rollback
        backend_str = self._get_backend()

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
        这个是判断值是否相等的 返回bool值
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


test_url = "mysql://localhost:3306/ry?useUnicode=&useJDBCCompliantTimezoneShift=&useLegacyDatetimeCode=&serverTimezone=PRC&characterEncoding=UTF8"
# a1 = DatabaseURL(test_url)

a2 = Database(test_url)
a2._get_backend()
