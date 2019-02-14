"""
Created by 你好 on 2019/1/19
"""
___author___ = '你好'

from flask import Flask
from app.models.book import db
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    # 配置文件的导入
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    # 蓝图的注册
    register_blueprint(app)

    # 数据库的注册
    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    return app


# 蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
