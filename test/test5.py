"""
Created by 你好 on 2019/1/23
"""
import threading
import time

___author___ = '你好'

from werkzeug.local import Local


class A:
    b = 1


my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    # 新线程
    print("in  new thread b is " + str(my_obj.b))


new_t = threading.Thread(target=worker)
new_t.start()
time.sleep(1)
# 主线程
print('in main thread b is ' + str(my_obj.b))
