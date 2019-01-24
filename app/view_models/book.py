"""
 Hello 

"""


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls.__cut_book_data(book)
                                 for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'price': data['price'],
            'summary': data['summary'],
            'author': '、'.join(data['author']),
            'image': data['image']

        }
        return book
