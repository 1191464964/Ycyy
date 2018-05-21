# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-17
import os
from flask import (Flask,request....)
"""


class RegisterModelView:

    def __init__(self):
        self.code = 400
        self.msg = '无正确数据!'
        self.data = []

    def fill(self, items_data=None):
        if items_data:
            self.data = items_data
            self.code = 201
            self.msg = "注册用户成功!"
