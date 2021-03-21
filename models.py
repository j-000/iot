from sqlalchemy.orm import (
    declarative_base
)
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    String,
    Text
)
import datetime
from server import db


Base = declarative_base()


class Entry(Base):

    __tablename__ = 'entries'

    query = db.query_property()
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(), default=datetime.datetime.utcnow())
    data = Column(Text())

    def __init__(self, data):
        self.data = data
        db.add(self)
        db.commit()
