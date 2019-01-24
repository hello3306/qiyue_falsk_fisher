"""
Created by 你好 on 2019/1/19
"""
from wtforms.validators import length, NumberRange, DataRequired

___author___ = '你好'

from wtforms import Form, StringField, IntegerField


class SearchFrom(Form):
    # 参数验证
    # message 错误提示
    # default 默认值设置
    # DataRequired 验证空格
    q = StringField(validators=[DataRequired(), length(min=1, max=30, message='参数错误')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
