# -*- coding: utf-8 -*-
from datetime import datetime
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class _Base(db.Model):
    __abstract__ = True
    deleted = db.Column(db.SmallInteger, default=0)  # 逻辑删除:0表示显示，1表示删除
    active = db.Column(db.SmallInteger, default=0)  # 禁用/启用:0表示显示，1表示删除


class Base(_Base):
    """
    继承_Base类
    :author lyfy
    :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    imagePaths = db.Column(db.String(50), unique=True, doc="项目图片地址")
    title = db.Column(db.String(50), unique=True, nullable=True, doc="标题")
    insertTime = db.Column(db.DateTime, default=datetime.utcnow, doc="时间")
    pubtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    shortContent = db.Column(db.Text, nullable=True, doc="文章内容")
    source = db.Column(db.String(255), unique=True, nullable=True, doc="文章来源")  # 来源

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # hasattr(self,key) # 是否包含key
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)  # 给key赋值value （将value的值赋给key）


class User(_Base):
    """
    用户表
    """
    __tablename__ = "user"
    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    username = db.Column(db.String(40), unique=True, nullable=False, doc="用户名")
    email = db.Column(db.String(40), unique=True, nullable=False, doc="邮箱")
    phone = db.Column(db.Integer, doc="电话号码")
    resume_url = db.String(db.String(255))
    _password = db.Column('password', db.String(256), nullable=False, doc="密码")
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    cmember = db.relationship('Cmember', uselist=False)  # 主键

    def __repr__(self):
        return '<Admin:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY

    @property
    def is_active(self):
        if self.active == 0:
            return "禁用"
        else:
            return "启用"

    @classmethod
    def get_alluser(self):
        return User.query.filter_by(deleted=0).all()

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # hasattr(self,key) # 是否包含key
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)  # 给key赋值value （将value的值赋给key）


class Cmember(Base):
    """
    部委
    author:lyfy
    :return:[<Cmember:XXX>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Cmember:{}>'.format(self.title)


class Local(Base):
    """
    地方
    @author lyfy
    :return:[<Local:XXX>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Local:{}>'.format(self.title)


class SocioGroup(Base):
    """
    社会团体
    @author lyfy
    :return:[<SocioGroup:xxx>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<SocioGroup:{}>'.format(self.title)


class BaseCity(Base):
    """
    基地
    @author lyfy
    :return:[<BaseCity:xxx>]
    """
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<BaseCity:{}>'.format(self.title)


class Panalysis(_Base):
    """"
    政策分析
    @author lyfy
    :return:[<Panalysis:xxx>]
    """
    businessId = db.Column(db.Integer, primary_key=True, doc="id")
    title = db.Column(db.String(50), unique=True, nullable=False, doc="标题")
    type = db.Column(db.Integer, doc="type状态码")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Panalysis:{}>'.format(self.title)


class Atracking(_Base):
    """"
    活动跟踪
    @author lyfy
    :return:[<Atracking:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    category = db.Column(db.String(50), unique=True, doc="cate状态码")
    picPath = db.Column(db.String(50), unique=True, doc="图片地址")
    source = db.Column(db.String(50), unique=True, doc="文章来源")  # 来源
    publishTime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Atracking:{}>'.format(self.title)


class Scolumn(_Base):
    """
    专题专栏
    @author lyfy
    :return:[<Scolumn:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    type = db.Column(db.Integer, doc="type状态码")
    category = db.Column(db.Integer, doc="category状态码")
    pubTime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Scolumn:{}>'.format(self.title)


class Broadcast(_Base):
    """"
    轮播图
    @author lyfy
    :return:[<Broadcast:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增id")
    title = db.Column(db.String(50),unique=True, doc="文章标题")
    imagePaths = db.Column(db.String(200), unique=True, doc="图片地址")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="外键")  # 外键

    def __repr__(self):
        return '<Broadcast:{}>'.format(self.title)


class Lpolicy(_Base):
    """"
    最新政策
    @author lyfy
    :return:[<Lpolicy:xxx>]
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(50), unique=True, nullable=True, doc="文章标题")
    pubtime = db.Column(db.DateTime, default=datetime.utcnow, doc="发布时间")
    shortContent = db.Column(db.Text, doc="文章正文")
    source = db.Column(db.String(255), doc="文章来源")  # 来源
    issuedno = db.Column(db.String(50)) #发改运行〔xxx〕xxx号
    issuedtime = db.Column(db.DateTime, default=datetime.utcnow)
    link = db.Column(db.String(255))  #不知名网址
    type = db.Column(db.Integer, doc="type状态码")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), doc="引用外键")  # 外键
    def __repr__(self):
        return '<Lpolicy:{}>'.format(self.title)


class ServiceExpansion(_Base):
    """
    服务拓展
    @author:lyfy
    :return:
    """
    id = db.Column(db.Integer, primary_key=True, doc="自增ID")
    title = db.Column(db.String(50), unique=True, doc="文章标题")
    pubtime = db.Column(db.DateTime,default=datetime.utcnow, doc="发布时间")
    shortContent = db.Column(db.String(255), doc="正文内容")
    source = db.Column(db.String(255), doc="文章来源")
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), doc="引用外键")
    def __repr__(self):
        return '<ServiceExpansion:{}>'.format(self.title)