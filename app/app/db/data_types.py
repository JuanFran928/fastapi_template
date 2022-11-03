import json
from datetime import datetime

from app.core.config import settings
from sqlalchemy import Enum, TypeDecorator
from sqlalchemy.dialects.mysql import (
    DATE,
    DATETIME,
    DECIMAL,
    ENUM,
    INTEGER,
    LONGTEXT,
    MEDIUMINT,
    MEDIUMTEXT,
    NUMERIC,
    REAL,
    SMALLINT,
    TEXT,
    TINYINT,
    TINYTEXT,
    VARCHAR,
)

# if settings.TESTING_MODE:

#     class TextDateTime(TypeDecorator):
#         impl = DATETIME
#         cache_ok = True

#         def process_bind_param(self, value, dialect):
#             if value is not None:
#                 value = datetime.fromisoformat(value)
#             return value

#         def process_result_value(self, value, dialect):
#             return value

#     DATETIME = TextDateTime
#     TINYINT = INTEGER
#     SMALLINT = INTEGER
#     MEDIUMINT = INTEGER
#     DECIMAL = REAL
#     VARCHAR = TEXT
#     TINYTEXT = TEXT
#     MEDIUMTEXT = TEXT
#     LONGTEXT = TEXT


class TextJSON(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        else:
            value = {}
        return value


class TextArray(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        else:
            value = []
        return value


class Timestamp(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = str(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = int(value)
        return value


ENUM = Enum
TEXTJSON = TextJSON
TEXTARRAY = TextArray
TIMESTAMP = Timestamp
