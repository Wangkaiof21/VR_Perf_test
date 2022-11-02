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
        pass


class DatabaseURL:
    def __init__(self, url: typing.Union[str, "Database"]):
        if isinstance(url, DatabaseURL):
            self.url: str = url._url
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
        return self._components