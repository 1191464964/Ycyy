# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-17
import os
from flask import (Flask,request....)
"""
from werkzeug.security import safe_str_cmp

from innp_app.models import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
