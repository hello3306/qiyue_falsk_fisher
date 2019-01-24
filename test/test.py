"""
Created by 你好 on 2019/1/20
"""
___author___ = '你好'


class MyResource:

    def __enter__(self):
        print('链接资源')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('关闭资源链接')
        b = 2
        return b

    def query(self):
        print('查询资源')


with MyResource() as resource:
    resource.query()
    pass
