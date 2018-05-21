# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from .config import configs
from .models import db


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)


def register_blueprints(app):
    from .apps import index, icnpp
    app.register_blueprint(index)
    app.register_blueprint(icnpp, url_prefix='/admin')


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)  # 注册路由
    register_extensions(app)  # 数据库热迁移
    Swagger(app)  # 使用Swagger

    return app
