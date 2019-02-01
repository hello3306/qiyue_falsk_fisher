"""
Created by 你好 on 2019/1/19
"""
from flask import Blueprint

___author___ = '你好'

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
