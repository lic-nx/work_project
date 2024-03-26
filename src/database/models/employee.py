import uuid
from database.base import Base
from datetime import datetime
from alembic import op

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




Employee_Group = Table( # связь работников и их группы
    "emploe_group",
    Base.metadata,
    Column("id", ForeignKey("group_workers.id")),
    Column("emploeer_id", ForeignKey("workers.id"))
)




class Group(Base):
    __tablename__ = "group_workers"
    id = Column(Integer, primary_key=True, unique=True )
    name = Column(String, default="")



class Employee(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, unique=True)
    full_name = Column(String, default="")
    post = Column(String, default="")
    personal_phone = Column(String, default="")
    mail = Column(String, default="")
    work_phone = Column(String, default="")
    internal_phone = Column(String, default="")
    telegramm = Column(String, default="")
    skype = Column(String, default="")
    bitrix24 = Column(String, default="")
    division = Column(String, default="")
    birthday = Column(DateTime, default="")
    personal_photo =Column(String, default="")
    group = relationship( 
        "Group",
        secondary=Employee_Group, 
        backref="workers"
        
    ) # группа к которой относится человек надо будет сделать связь с другой таблицей


def upgrade():
    op.execute("INSERT INTO workers(id, full_name, post, personal_phone, mail, work_phone, internal_phone, telegramm, skype, bitrix24, division, birthday ) \
              VALUES (1, 'John Smith', 'важный хуй', '+78945632541', '4563', '@ddd', 'F', 'cvsd', '121', '12-05-2007) ")

# op.bulk_insert(
#    Employee ,
#     [
#         {
#             "id": 1,
#             "full_name": "John Smith",
#             "post": "важный хуй",
#             "personal_phone":"+78945632541",
#             "mail":"maam@mama.ru",
#             "work_phone":"78965412352",
#             "internal_phone":"4563",
#             "telegramm":"@ddd",
#             "skype":"F'",
#             "bitrix24":"cvbn",
#             "division":"121",
#             "birthday":"27-05-2007"
#         # },
#         # {
#         #     "id": 2,
#         #     "name": "Ed Williams",
#         #     "create_date": date(2007, 5, 27),
#         # },
#         # {
#         #     "id": 3,
#         #     "name": "Wendy Jones",
#         #     "create_date": date(2008, 8, 15),
#         },
#     ],
# )