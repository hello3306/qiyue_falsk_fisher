"""
Created by 你好 on 2019/1/23
"""
import time

___author___ = '你好'

import threading


def work():
    print('I am  thread')
    t = threading.current_thread()
    # 程序休眠100秒
    time.sleep(100)
    print(t.getName())


new_t = threading.Thread(target=work, name='hello')
new_t.start()

# print("线程")
t = threading.current_thread()
print(t.getName())
