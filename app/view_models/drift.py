"""
 Hello 

"""
from flask_login import current_user


class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = {}
        pass

    @staticmethod
    def requerter_or_gifter(drift, current_user_id):
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gift'
        return you_are

    def __parse(self, drift, current_user_id):
        you_are = self.requerter_or_gifter(drift, current_user_id)
        r = {
            'you_are': you_are,
            ' drift_id': drift.id,
            ' book _title': drift.book_title,
            ' book_author': drift.book_author,
            ' book_img': drift.book_img,
            ' date': drift.create_datetime.strftime('%Y-%m-%d'),
            'operator': drift.requester_nickname if you_are != 'requester' else drift.gifter_nickname,
            ' message': drift.message,
            ' address': drift.address,
            ' recipient_name': drift.recipient_name,
            ' mobile': drift.mobile,
            ' status': drift.pending
        }


