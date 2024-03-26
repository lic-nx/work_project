import uuid
from database.base import Base
from datetime import datetime
from database.models.employee import *
from database.models.clients import *
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

manager_group = Table( # связь с таблицей работники
    "manager_in_proj",
    Base.metadata,
    Column("emploeer_id", ForeignKey("workers.id")),
    Column("carts_id", ForeignKey("carts_info.id"))
)

responsible_group = Table( # связь с таблицей работники
    "responsible_in_proj",
    Base.metadata,
    Column("emploeer_id", ForeignKey("workers.id")),
    Column("carts_id", ForeignKey("carts_info.id"))
)


participants_group = Table( # связь с таблицей работники
    "participants_in_proj",
    Base.metadata,
    Column("emploeer_id", ForeignKey("workers.id")),
    Column("carts_id", ForeignKey("carts_info.id"))
)



clients_group = Table( # связь с таблицей клиенты
    "clients_group_in_proj",
    Base.metadata,
    Column("clients_id", ForeignKey("clients.id")),
    Column("carts_id", ForeignKey("carts_info.id"))
)

class Carts(Base):
    __tablename__ = "carts_info"
    id = Column(Integer, primary_key=True, unique=True)
    
    # manager = relationship( 
    #     "Employee",
    #     secondary=manager_group,
    #     backref="carts_info"
    # )
    # отношения с таблицей сотрудники

    # responsible = relationship( 
    #     "Employee",
    #     secondary=responsible_group,
    #     backref="carts_info"
    # )
    
    # participants = relationship( 
    #     "Employee",
    #     secondary=participants_group,
    #     backref="carts_info"
    # )
    company = Column(String, default="")
    address = Column(String, default="")
    file_path = Column(String, default="")
    delivered = Column(DateTime, default="") # поставлена 
    contract_number = Column(String, default="")
    # contacts = relationship( 
    #     "clients",
    #     secondary=clients_group,
    #     backref="carts_info"
    # )