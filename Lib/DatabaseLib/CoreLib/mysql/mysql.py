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
        self._database_url = DatabaseURL
