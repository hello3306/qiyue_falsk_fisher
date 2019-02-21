"""
Created by 你好 on 2019/1/19
"""
from wtforms.validators import length, NumberRange, DataRequired, Regexp

___author___ = '你好'

from wtforms import Form, StringField, IntegerField


class SearchFrom(Form):
    # 参数验证
    # message 错误提示
    # default 默认值设置
    # DataRequired 验证空格
    q = StringField(validators=[DataRequired(), length(min=1, max=30, message='参数错误')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = \
        StringField(
            '收件人姓名', validators=[DataRequired(),
                                 length(min=2, max=20,
                                        message='收件人姓名必须在2到20个字符之间')])
    mobile = \
        StringField(validators=[DataRequired(),
                                Regexp('^1[0-9]{10}$',
                                       0, '请输入正确的手机号')])
    message = StringField()
    address = \
        StringField(validators=[DataRequired(),
                                length(min=10,
                                       max=70,
                                       message='地址不到10个字吗？写详细些吧')])
