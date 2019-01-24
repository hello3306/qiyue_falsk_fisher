"""
 Hello 

"""


class BookViewModel:

    def package_single(self, data, keyword):
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned['total'] = 1
        pass

    def package_collection(self, data, keyword):
        pass

    def __cut_book_data(self, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'price': data['price'],
            'summary': data['summary'],
            'author': '、'.join(data['author']),
            'image': data['image']

        }
        pass
