import uuid
from database.base import Base
from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    Table,
    ForeignKey,
    DECIMAL,
    Boolean,
    Enum,
    JSON,
    DateTime
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, unique=True)
    full_name = Column(String, default="")
    post = Column(String, default="")
    personal_phone = Column(String, default="")
    mail = Column(String, default="")
   
 