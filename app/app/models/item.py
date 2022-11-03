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
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Item(ORMBase):
    id = Column(INTEGER(10, unsigned=True), primary_key=True, nullable=False)
    title = Column(VARCHAR(length=255), nullable=True)
    description = Column(VARCHAR(length=255), nullable=True)
    owner_id = Column(INTEGER(10, unsigned=True), ForeignKey("user.id"), index=True)
    owner = relationship("User", back_populates="items")
