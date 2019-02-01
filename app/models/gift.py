"""
 Hello 

"""
from tokenize import String

from sqlalchemy import Column, Integer, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationships

from app.models.base import Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
