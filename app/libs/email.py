"""
Created by 你好 on 2019/2/20
"""
from threading import Thread

from flask import current_app, render_template, app

___author___ = '你好'
from app import mail
from flask_mail import Message


# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            raise e


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1176837406@qq.com', body='Test',
    #               recipients=['1176837406@qq.com'])
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    # mail.send(msg)
