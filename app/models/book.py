"""
Created by 你好 on 2019/1/20
"""
___author___ = '你好'

from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

# flask-sqlalchemy flask 操作数据库

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    image = Column(String(50))
