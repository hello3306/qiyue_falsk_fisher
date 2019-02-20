"""
Created by 你好 on 2019/2/20
"""
from flask import current_app, render_template

___author___ = '你好'
from app import mail
from flask_mail import Message


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='1176837406@qq.com', body='Test',
    #               recipients=['1176837406@qq.com'])
    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
