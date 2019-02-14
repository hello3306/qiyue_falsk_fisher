from flask import current_app, flash

from app.models.base import db
from app.models.gift import Gift
from . import web

__author__ = '七月'

from flask_login import login_required, current_user


@web.route('/my/gifts')
# 登录了才能操作
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # 事物
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            # 事物回滚
            db.session.rollback()
            # 抛出异常
            raise e

    else:
        flash('这本书已经添加至赠送清单或在你的心愿清单了，请不要重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
