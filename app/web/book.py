"""
Created by 你好 on 2019/1/19
"""
import json

___author___ = '你好'
from flask import jsonify, request
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
        return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        return jsonify(form.errors)
