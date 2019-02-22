"""
Created by 你好 on 2019/2/21
"""
from enum import Enum

___author___ = '你好'


# 枚举

class PendingStatus(Enum):
    # 交易状态
    waiting = 1
    success = 2
    reject = 3
    redraw = 4

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            1: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            2: {
                'requester': '对方已邮寄',
                'gifter': '你邮寄'
            },
            3: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'

            },
            4: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            }
        }
        return key_map[status][key]
