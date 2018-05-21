# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from flask import Blueprint

from .icnpp import IndexView, Register,LoginView

icnpp = Blueprint('icnpp', __name__)

icnpp.add_url_rule(
    '/',
    view_func=IndexView.as_view('/'),
    endpoint="innp_only_andminindex",
    methods=["POST", "GET"]
)

icnpp.add_url_rule(
    '/register',
    view_func=Register.as_view('register'),
    endpoint="innp_only_register",
    methods=["POST"]
)

icnpp.add_url_rule(
    '/login',
    view_func=LoginView.as_view('login'),
    methods=["POST"]
)