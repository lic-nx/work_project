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


# employee_group = Table('employee_group', Base.metadata,
#     Column('employee_id', ForeignKey('employee_info.id'), primary_key=True),
#     Column('carts_id', ForeignKey('carts_info.id'), primary_key=True)
# )

# services = Table('services', Base.metadata,
#     Column('service_id', ForeignKey('services_info.id'), primary_key=True),
#     Column('carts_id', ForeignKey('carts_info.id'), primary_key=True)
# )

# class Services(Base):
#     __tablename__ = "services_info"
#     id = Column(Integer, primary_key=True, unique=True)
#     name = Column(Integer, primary_key=True, unique=True)


class Employee(Base):
    # __tablename__ = "workers"
    # id = Column(Integer, primary_key=True, unique=True)
    # full_name = Column(String, default="")
    # post = Column(String, default="")
    # personal_phone = Column(String, default="")
    # mail = Column(String, default="")
    # work_phone = Column(String, default="")
    # internal_phone = Column(String, default="")
    # telegramm = Column(String, default="")
    # skype = Column(String, default="")
    # bitrix24 = Column(String, default="")
    # division = Column(String, default="")
    # birthday = Column(DateTime, default="")
    # personal_photo =Column(String, default="")
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, unique=True)
    name           =Column(String)
    last_name      =Column(String)
    second_name    =Column(String)
    active         =Column(Boolean)
    work_position  =Column(String)
    last_login     =Column(String)
    date_register  =Column(String)
    personal_photo =Column(String)

# в базе должны быть такие же столбцы

# class Carts(Base):
#     __tablename__ = "carts_info"
#     id = Column(Integer, primary_key=True, unique=True)
    
#     manager = Column(String, default="")
#     # отношения с таблицей сотрудники

#     responsible = relationship( 
#         "Employee",
#         secondary=employee_group,
#         backref="carts_info"
#     )
#     participants = relationship( 
#         "Participants",
#         secondary=employee_group,
#         backref="carts_info"
#     )
#     type_of_service = relationship( 
#         "type_of_service",
#         secondary=services,
#         backref="carts_info"
#     ) # тип услуги  возможно надо сделать зависимости
#     company = Column(String, default="")
#     address = Column(String, default="")
#     customer_full_name = Column(String, default="")
#     telegramm = Column(String, default="")
#     mail = Column(String, default="")
#     path_folder = Column(String, default="")
#     delivered = Column(DateTime, default="")
#     contract_number = Column(DateTime, default="")
#     color = Column(String, default="")
    