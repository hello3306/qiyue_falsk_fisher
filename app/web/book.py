"""
Created by 你好 on 2019/1/19
"""
___author___ = '你好'
from flask import jsonify, request
from app.spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key
from . import web
from app.froms.book import SearchFrom


@web.route('/book/search')
def search():
    # 验证传入的值
    form = SearchFrom(request.args)
    if form.validate():
        # .strip()去除空格
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
