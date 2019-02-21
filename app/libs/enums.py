"""
Created by 你好 on 2019/2/21
"""
from enum import Enum

___author___ = '你好'


# 枚举

class PendingStatus(Enum):
    # 交易状态
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
