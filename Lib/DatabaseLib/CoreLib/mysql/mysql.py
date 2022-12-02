import getpass
import logging
import typing
import uuid
from abc import ABC

import aiomysql
from sqlalchemy.dialects.mysql import pymysql
from sqlalchemy.engine.cursor import CursorResultMetaData
from sqlalchemy.engine.interfaces import Dialect, ExecutionContext
from sqlalchemy.engine.row import Row
from sqlalchemy.sql import ClauseElement
from sqlalchemy.sql.ddl import DDLElement

from Lib.DatabaseLib.CoreLib.core import LOG_EXTRA, DatabaseURL
from Lib.DatabaseLib.CoreLib.interfaces import (
    ConnectionBackend,
    DatabaseBackend,
    Record,
    TransactionBackend,
)


class MySQLBackend(DatabaseBackend):
    def __init__(self, database_url: typing.Union[DatabaseURL, str], **options: typing.Any) -> None:
        self._database_url = DatabaseURL(database_url)
        self._options = options
        self.dialect = pymysql.dialect(paramstyle="pyformat")
        self.dialect.supports_native_decimal = True
        self._pool = None

    def _get_connection_kwargs(self) -> dict:
        url_options = self._database_url.options
        kwargs = {}
        min_size = url_options.get("min_size")
        max_size = url_options.get("max_size")
        pool_recycle = url_options.get("pool_recycle")
        ssl = url_options.get("ssl")
        if min_size is not None:
            kwargs["min_size"] = int(min_size)
        if max_size is not None:
            kwargs["max_size"] = int(max_size)
        if pool_recycle is not None:
            kwargs["pool_recycle"] = int(pool_recycle)
        if ssl is not None:
            kwargs["ssl"] = {"true": True, "false": False}[ssl.lower()]
        for key, value in self._options.items():
            if key == "min_size":
                key = "minsize"
            elif key == "max_size":
                key = "maxsize"
            kwargs[key] = value
        return kwargs

    async def connect(self) -> None:
        assert self._pool is None, "DatabaseBackend is already running"
        kwargs = self._get_connection_kwargs()
        self._pool = self._get_connection_kwargs()
        self._pool = await aiomysql.create_pool(
            host=self._database_url.hostname,
            port=self._database_url.port or 3306,
            user=self._database_url.username or getpass.getuser(),
            password=self._database_url.password,
            db=self._database_url.database,
            autocommit=True,
            **kwargs

        )

    async def disconnect(self) -> None:
        assert self._pool is not None, "DatabasesBackend is not running"
        self._pool.close()
        await self._pool.wait_closed()
        self._pool = None

    def connection(self) -> "ConnectionBackend":
        return MySQLConnection(self, self._dialect)


class CompilationContext:
    def __init__(self, context: ExecutionContext):
        self.context = context

class MySQLConnection:
    def __init__(self, context: ExecutionContext):
        self.context = context

    async def
