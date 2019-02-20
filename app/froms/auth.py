"""
 Hello 

"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, length, ValidationError

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), length(6, 32)])

    nickname = StringField(validators=(DataRequired(),
                                       length(2, 10, message='昵称至少需要两个字符，最多10个字符')))

    # 自定义的验证器
    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, filed):
        if User.query.filter_by(nickname=filed.data).first():
            raise ValidationError('昵称已被注册')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空，请输入你的密码'), length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), length(8, 64),
                                    Email(message='电子邮箱不符合规范')])
