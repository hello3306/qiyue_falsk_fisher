"""
 Hello 

"""

from sqlalchemy import Column, Integer, Boolean, ForeignKey, SmallInteger,String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationships('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
