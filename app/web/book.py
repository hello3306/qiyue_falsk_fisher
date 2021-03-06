"""
Created by 你好 on 2019/1/19
"""
import json

from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import TradeInfo

___author___ = '你好'
from flask import jsonify, request, render_template, flash
from app.spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key
from . import web
from app.froms.book import SearchFrom
from app.view_models.book import BookViewModel, BookCollection


@web.route('/book/search')
def search():
    # 验证传入的值
    form = SearchFrom(request.args)
    books = BookCollection()
    if form.validate():
        # .strip()去除空格
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, page)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍的详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:

        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True

        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)


@web.route('/test')
def test():
    r = {
        'name': 'hello',
        'age': 22
    }
    flash('hello,lj', category='error')
    flash('hello,lj2', category='waring')
    # return jsonify(r)
    return render_template('test.html', data=r)
