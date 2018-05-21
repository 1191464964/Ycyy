# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from datetime import timedelta

from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token

from innp_app.models import db, User
from innp_app.common.rest import RestView


class IndexView(RestView):
    decorators = [jwt_required, ]

    def get(self):
        """
        后台显示内容
        ---
        tags:
          - 后台页面
        """

        data = {
            "users": [{
                "username": "11111"
            },
                {
                    "username": "w22"}
            ]
        }
        return {
                   "data": data
               }, 200

    def post(self):
        # 后端主页面的所有数据展示
        pass


class Register(RestView):
    def post(self):
        with db.auto_commit():
            user = User()
            user.set_attrs(request.form)
            db.session.add(user)
            try:
                access_token = create_access_token(identity=request.form['username'], expires_delta=timedelta(days=30))
                return {
                           'message': '用户 {} 创建成功'.format(request.form['username']),
                           'access_token': access_token
                       }, 201
            except:
                return None


class LoginView(RestView):
    def post(self):
        user = User.query.filter_by(username=request.form["username"]).first()
        access_token = create_access_token(identity=request.form['username'], expires_delta=timedelta(days=30))
        data = {
                   "msg": [{
                       "username": request.form["username"],
                       "_access_token": access_token
                   }],
                   "code": 200
               }, 200
        return data if user and user.check_password(request.form["password"]) else {"msg": "用户名或密码错误!"}
