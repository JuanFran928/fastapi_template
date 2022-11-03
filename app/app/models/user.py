from app.db.base import ORMBase
from app.db.data_types import (
    DATETIME,
    ENUM,
    INTEGER,
    MEDIUMTEXT,
    TEXTARRAY,
    TEXTJSON,
    TINYTEXT,
    VARCHAR,
)
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(ORMBase):
    id = Column(INTEGER(10, unsigned=True), primary_key=True, nullable=False)
    full_name = Column(VARCHAR(length=255), nullable=True)
    email = Column(VARCHAR(length=255), nullable=False)
    hashed_password = Column(VARCHAR(length=128), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
