# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
import time
from datetime import timedelta
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from innp_app.serializers import *
from datetime import datetime
from innp_app.models import (db, User, Mediamanage, ActivityManage, Mascot, Guest, Hall, ActivityType, CenterNew,
                             LocalNew, Department, policy, LocalReport, PolicyRelease, Ecosphere, TimerShaft,
                             BusinessService, AreaService, SubjectClassification, PolicyClassify, IndustrialPark,
                             BaseManage,
                             UserBrowsingMessage, UserSearchInfo, PilotManagement, Suggestions,
                             PolicyStatistics, JournalSystem, JournalPolicy, AboutUs,
                             MovePresentation, MoveService, MoveHomePage, MoveVersion,
                             MoveUser, MoveBriefing, GuideToAffairs, GovernmentFunds,
                             FavouredPolicy, CancellationAndDecentralization)
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

class MediaView(RestView):
    def AddMedia(self):
        """
        媒体管理，新增媒体请求处理并响应
        author:wpc
        :return:
        """
        with db.auto_commit():
            # ms = Mediamanage('10', '样例测试', '医药', '音频', '10', 'www.baidu.com', '已置顶')
            ma = Mediamanage()
            ma.id = 10
            ma.meidaName = "样例测试"
            ma.bussionessType = "医药"
            ma.mediaType = "音频"
            ma.sort = "10"
            ma.href = "www.baidu.com"
            ma.top = "已置顶"
            db.session.add(ma)
            return "1111", 200


class ActivityManageView(RestView):
    """
    活动管理
    author:wpc
    """

    def addmanage(self):
        """
        添加活动管理
        author:wpc
        :return:
        """
        with db.auto_commit():
            amanage = ActivityManage()
            amanage.id = 9
            amanage.activityTitle = "事业培训"
            amanage.activityType = "教育"
            amanage.area = "北京"
            amanage.activity = "关于加强事业单位人员工作能力"
            amanage.releaseUnit = "教育局"
            amanage.releasePeople = "张三"
            amanage.releaseTime = "2018年5月21日"
            amanage.source = "教育局"
            amanage.mkdirTime = "2018年5月12日"
            amanage.modifer = "张三"
            amanage.modifyTime = "2018年5月13日"
            db.session.add(amanage)
            return "1111", 200


class MascotView(RestView):
    """
    吉祥物管理
    author:wpc
    """

    def addmascot(self):
        """
        新增吉祥物
        :return:
        """
        mascot = Mascot()
        mascot.id = 8
        mascot.title = "吉祥物"
        mascot.intro = "奥运福娃"
        mascot.releasePeople = "发布人，张三"
        mascot.releaseTime = '%2018-%4-%23'
        mascot.mkdirTime = '%2018-%4-%21'
        mascot.modifer = "李四"
        mascot.modifyTime = '%2018-%5-%22'
        mascot.sort = 8
        mascot.top = "已置顶"
        mascot.releaseNote = "已标识"
        db.session.add(mascot)
        return "1111", 200

    def deletemascot(self):
        """
        删除吉祥物
        :return:
        """
        mascotlist = Mascot.query.filter_by(id="7").all()
        for m in mascotlist:
            m.active = 1


class GuestView(RestView):
    """
    嘉宾管理
    author:wpc
    """

    def addguest(self):
        guest = Guest()
        guest.id = 20
        guest.title = "嘉宾管理标题"
        guest.activityType = "活动类"
        guest.publisher = "张三"
        guest.releaseTime = '%2018-%5-%23'
        guest.mkdirTime = '%2018-%5-%21'
        guest.modifer = "李四"
        guest.modifyTime = "%2018-%5-%24"
        guest.sort = 20
        guest.top = "已置顶"
        guest.releaseNote = "已标识"
        db.session.add(guest)


class HallView(RestView):
    """
    展厅管理
    author:wpc
    """

    def addhall(self):
        """
        添加展厅管理
        author:wpc
        :return:
        """
        hall = Hall()
        hall.id = 23
        hall.title = "添加展厅"
        hall.intro = "添加展厅活动相关信息"
        hall.releasePeople = "张三"
        hall.releaseTime = "%2018-%5-%21"
        hall.mkdirTime = "%2018-%5-%21"
        hall.modifier = "李四"
        hall.modifyTime = "%2018-%5-%21"
        hall.sort = 23
        hall.top = "已置顶"
        hall.releaseNote = "已标识"
        db.session.add(hall)


class ActivityTypeView(RestView):
    def addactivitytype(self):
        """
        活动类别管理
        author:wpc
        :return:
        """
        atype = ActivityType()
        atype.id = 24
        atype.activityTitle = "活动类别管理标题"
        atype.activityType = "活动类别类型"
        atype.activityIntro = "活动简介"
        atype.releasePeople = "张三"
        atype.releaseTime = "%2018-%5-%21"
        atype.modifier = "李四"
        atype.updateTime = "%2018-%5-%21"
        atype.status = "已启用"
        atype.pageView = 300
        atype.href = "www.baidu.com"
        db.session.add(atype)


class CenterNewView(RestView):
    """
    中央快讯
    author:wpc
    """

    def addcenternew(self):
        """
        添加中央快讯
        author:wpc
        :return:
        """
        cnew = CenterNew()
        cnew.id = 25
        cnew.title = "中央快讯信息"
        cnew.intro = "中央快讯简介"
        cnew.releaseTime = "%2018-%5-%21"
        cnew.mkdirTime = "%2018-%5-%21"
        cnew.modifyTime = "%2018-%5-%21"
        cnew.sort = 25
        cnew.releaseNote = "已标识"
        cnew.top = "已置顶"
        cnew.source = "中央"
        db.session.add(cnew)


class LocalNewView(RestView):
    """
    地方报道
    author:wpc
    """

    def addlocalnew(self):
        """
        发布地方报道
        author:wpc
        :return:
        """
        lnew = LocalNew()
        lnew.id = 26
        lnew.title = "地方报道消息"
        lnew.intro = "地方报道简介"
        lnew.releaseTime = "%2018-%5-%21"
        lnew.mkdirTime = "%2018-%5-%21"
        lnew.modifyTime = "%2018-%5-%21"
        lnew.sort = 26
        lnew.releaseNote = "已标识"
        lnew.top = "已置顶"
        lnew.source = "来源"
        db.session.add(lnew)


class DepartmentView(RestView):
    """
    部委讯息
    author:wpc
    """

    def adddepartment(self):
        """
        发布部委讯息
        author:wpc
        :return:
        """
        d = Department()
        d.id = 27
        d.title = "部委讯息"
        d.intro = "部委讯息简介"
        d.releaseTime = "%2018-%5-%21"
        d.mkdirTime = "%2018-%5-%21"
        d.modifyTime = "%2018-%5-%21"
        d.sort = 27
        d.releaseNote = "已标识"
        d.top = "已置顶"
        d.source = "资料来源"
        db.session.add(d)


class policyView(RestView):
    """
    政策讯息
    author:wpc
    """

    def Addpolicy(self):
        """
        发布政策讯息
        author:wpc
        :return:
        """
        p = policy()
        p.id = 28
        p.title = "政策讯息"
        p.intro = "政策讯息简介"
        p.releaseTime = "%2018-%5-%21"
        p.mkdirTime = "%2018-%5-%21"
        p.modifyTime = "%2018-%5-%21"
        p.sort = 28
        p.releaseNote = "已标识"
        p.top = "已置顶"
        p.source = "资料来源"
        db.session.add(p)


class LocalReportView(RestView):
    """
    地方报道
    author:wpc
    """

    def AddLocalReport(self):
        """
        发布地方报道
        author:wpc
        :return:
        """
        lreport = LocalReport()
        lreport.id = 28
        lreport.title = "测试"
        lreport.intro = "简介"
        lreport.releaseTime = "%2018-%5-%21"
        lreport.sort = 28
        lreport.top = "已置顶"
        lreport.releaseNote = "已标识"
        db.session.add(lreport)


# ↓↓↓↓↓↓政策发布
class PolicyReleaseAddView(RestView):
    def post(self):
        """
        政策发布--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            policyrelease = PolicyRelease(title=request.form['title'],
                                          number=request.form['number'],
                                          organization=request.form['organization'],
                                          publisher=request.form['publisher'],
                                          releaseTime=request.form['releaseTime'],
                                          modifyTime=request.form['modifyTime'],
                                          policyTheme=request.form['policyTheme'],
                                          animalKeyword=request.form['animalKeyword'],
                                          timerShaft=request.form['timerShaft'],
                                          policyBelong=request.form['policyBelong'],
                                          area=request.form['area'],
                                          businessPeople=request.form['businessPeople'],
                                          businessService=request.form['businessService'],
                                          profession=request.form['profession'],
                                          policySort=request.form['policySort'],
                                          policyTop=request.form['policyTop'],
                                          releaseFlag=request.form['releaseFlag'])
            db.session.add(policyrelease)
        return "已发布", 200


class PolicyReleaseDeleteView(RestView):
    def post(self):
        """
        政策发布--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = PolicyRelease.query.filter(PolicyRelease.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class PolicyReleaseUpdateView(RestView):
    def post(self):
        """
        政策发布--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = PolicyRelease.query.filter(PolicyRelease.id == request.form['id']).first()
            result.title = request.form['title'],
            result.number = request.form['number'],
            result.organization = request.form['organization'],
            result.publisher = request.form['publisher'],
            result.releaseTime = request.form['releaseTime'],
            result.modifyTime = request.form['modifyTime'],
            result.policyTheme = request.form['policyTheme'],
            result.animalKeyword = request.form['animalKeyword'],
            result.timerShaft = request.form['timerShaft'],
            result.policyBelong = request.form['policyBelong'],
            result.area = request.form['area'],
            result.businessPeople = request.form['businessPeople'],
            result.businessService = request.form['businessService'],
            result.profession = request.form['profession'],
            result.policySort = request.form['policySort'],
            result.policyTop = request.form['policyTop'],
            result.releaseFlag = request.form['releaseFlag']
        return "已修改", 200


class PolicyReleaseView(RestView):
    def post(self):
        """
        政策发布--查---时间检索未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        number = request.form['number']
        area = request.form['area']
        policyTop = request.form['policyTop']
        profession = request.form['profession']
        policyTheme = request.form['policyTheme']
        organization = request.form['organization']
        releaseFlag = request.form['releaseFlag']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
                'number': number,
                'area': area,
                'policyTop': policyTop,
                'profession': profession,
                'policyTheme': policyTheme,
                'organization': organization,
                'releaseFlag': releaseFlag
            },
            'rows': PolicyRelease.query.filter(PolicyRelease.title.like('%' + title + '%'),
                                               PolicyRelease.number.like('%' + number + '%'),
                                               PolicyRelease.area.like('%' + area + '%'),
                                               PolicyRelease.policyTop.like('%' + policyTop + '%'),
                                               PolicyRelease.profession.like('%' + profession + '%'),
                                               PolicyRelease.policyTheme.like('%' + policyTheme + '%'),
                                               PolicyRelease.organization.like('%' + organization + '%'),
                                               PolicyRelease.releaseFlag.like('%' + releaseFlag + '%'),
                                               PolicyRelease.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': PolicyRelease.query.filter(PolicyRelease.title.like('%' + title + '%'),
                                                PolicyRelease.number.like('%' + number + '%'),
                                                PolicyRelease.area.like('%' + area + '%'),
                                                PolicyRelease.policyTop.like('%' + policyTop + '%'),
                                                PolicyRelease.profession.like('%' + profession + '%'),
                                                PolicyRelease.policyTheme.like('%' + policyTheme + '%'),
                                                PolicyRelease.organization.like('%' + organization + '%'),
                                                PolicyRelease.releaseFlag.like('%' + releaseFlag + '%'),
                                                PolicyRelease.deleted == 0).count(),
            'totalPageCount': PolicyRelease.query.filter(PolicyRelease.title.like('%' + title + '%'),
                                                         PolicyRelease.number.like('%' + number + '%'),
                                                         PolicyRelease.area.like('%' + area + '%'),
                                                         PolicyRelease.policyTop.like('%' + policyTop + '%'),
                                                         PolicyRelease.profession.like('%' + profession + '%'),
                                                         PolicyRelease.policyTheme.like('%' + policyTheme + '%'),
                                                         PolicyRelease.organization.like('%' + organization + '%'),
                                                         PolicyRelease.releaseFlag.like('%' + releaseFlag + '%'),
                                                         PolicyRelease.deleted == 0).paginate(page=int(pageNum),
                                                                                              per_page=int(
                                                                                                  pageSize)).pages
        }
        content, errors = PolicyReleaseSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓生态圈维护
class EcosphereUpdateView(RestView):
    def post(self):
        """
        生态圈维护--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = Ecosphere.query.filter(Ecosphere.id == request.form['id']).first()
            result.ecosphereName = request.form['ecosphereName']
        return "已修改", 200


class EcosphereView(RestView):
    def post(self):
        """
        生态圈维护--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        ecosphereName = request.form['ecosphereName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'ecosphereName': ecosphereName
            },
            'rows': Ecosphere.query.filter(Ecosphere.ecosphereName.like('%' + ecosphereName + '%'),
                                           Ecosphere.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': Ecosphere.query.filter(Ecosphere.ecosphereName.like('%' + ecosphereName + '%'),
                                            Ecosphere.deleted == 0).count(),
            'totalPageCount': Ecosphere.query.filter(Ecosphere.ecosphereName.like('%' + ecosphereName + '%'),
                                                     Ecosphere.deleted == 0).paginate(page=int(pageNum),
                                                                                      per_page=int(
                                                                                          pageSize)).pages
        }
        content, errors = EcosphereSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓时间轴维护维护
class TimerShaftView(RestView):
    def post(self):
        """
        时间轴维护--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        timerShaftName = request.form['timerShaftName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'timerShaftName': timerShaftName
            },
            'rows': TimerShaft.query.filter(TimerShaft.timerShaftName.like('%' + timerShaftName + '%'),
                                            TimerShaft.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': TimerShaft.query.filter(TimerShaft.timerShaftName.like('%' + timerShaftName + '%'),
                                             TimerShaft.deleted == 0).count(),
            'totalPageCount': TimerShaft.query.filter(TimerShaft.timerShaftName.like('%' + timerShaftName + '%'),
                                                      TimerShaft.deleted == 0).paginate(page=int(pageNum),
                                                                                        per_page=int(
                                                                                            pageSize)).pages
        }
        content, errors = TimerShaftSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓行业数据维护维护
class BusinessServiceAddView(RestView):
    def post(self):
        """
        行业数据维护--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            businessservice = BusinessService(businessName=request.form['businessName'])
            db.session.add(businessservice)
        return "已发布", 200


class BusinessServiceDeleteView(RestView):
    def post(self):
        """
        行业数据维护--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = BusinessService.query.filter(BusinessService.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class BusinessServiceUpdateView(RestView):
    def post(self):
        """
        行业数据维护--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = BusinessService.query.filter(BusinessService.id == request.form['id']).first()
            result.businessName = request.form['businessName']
        return "已修改", 200


class BusinessServiceView(RestView):
    def post(self):
        """
        行业数据维护--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        businessName = request.form['businessName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'businessName': businessName
            },
            'rows': BusinessService.query.filter(BusinessService.businessName.like('%' + businessName + '%'),
                                                 BusinessService.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': BusinessService.query.filter(BusinessService.businessName.like('%' + businessName + '%'),
                                                  BusinessService.deleted == 0).count(),
            'totalPageCount': BusinessService.query.filter(BusinessService.businessName.like('%' + businessName + '%'),
                                                           BusinessService.deleted == 0).paginate(page=int(pageNum),
                                                                                                  per_page=int(
                                                                                                      pageSize)).pages
        }
        content, errors = BusinessServiceSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓区域数据维护维护
class AreaServiceAddView(RestView):
    def post(self):
        """
        区域数据维护--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            areaservice = AreaService(areaName=request.form['areaName'])
            db.session.add(areaservice)
        return "已发布", 200


class AreaServiceDeleteView(RestView):
    def post(self):
        """
        区域数据维护--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = AreaService.query.filter(AreaService.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class AreaServiceUpdateView(RestView):
    def post(self):
        """
        区域数据维护--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = AreaService.query.filter(AreaService.id == request.form['id']).first()
            result.areaName = request.form['areaName']
        return "已修改", 200


class AreaServiceView(RestView):
    def post(self):
        """
        区域数据维护--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        areaName = request.form['areaName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'areaName': areaName
            },
            'rows': AreaService.query.filter(AreaService.areaName.like('%' + areaName + '%'),
                                             AreaService.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': AreaService.query.filter(AreaService.areaName.like('%' + areaName + '%'),
                                              AreaService.deleted == 0).count(),
            'totalPageCount': AreaService.query.filter(AreaService.areaName.like('%' + areaName + '%'),
                                                       AreaService.deleted == 0).paginate(page=int(pageNum),
                                                                                          per_page=int(
                                                                                              pageSize)).pages
        }
        content, errors = AreaServiceSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓主题分类维护
class SubjectClassificationAddView(RestView):
    def post(self):
        """
        主题分类维护--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            subjectclassification = SubjectClassification(SubjectName=request.form['SubjectName'])
            db.session.add(subjectclassification)
        return "已发布", 200


class SubjectClassificationDeleteView(RestView):
    def post(self):
        """
        主题分类维护--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = SubjectClassification.query.filter(SubjectClassification.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class SubjectClassificationUpdateView(RestView):
    def post(self):
        """
        主题分类维护--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = SubjectClassification.query.filter(SubjectClassification.id == request.form['id']).first()
            result.SubjectName = request.form['SubjectName']
        return "已修改", 200


class SubjectClassificationView(RestView):
    def post(self):
        """
        主题分类维护--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        SubjectName = request.form['SubjectName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'SubjectName': SubjectName
            },
            'rows': SubjectClassification.query.filter(SubjectClassification.SubjectName.like('%' + SubjectName + '%'),
                                                       SubjectClassification.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': SubjectClassification.query.filter(SubjectClassification.SubjectName.like('%' + SubjectName + '%'),
                                                        SubjectClassification.deleted == 0).count(),
            'totalPageCount': SubjectClassification.query.filter(
                SubjectClassification.SubjectName.like('%' + SubjectName + '%'),
                SubjectClassification.deleted == 0).paginate(page=int(pageNum),
                                                             per_page=int(
                                                                 pageSize)).pages
        }
        content, errors = SubjectClassificationSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓政策分类维护
class PolicyClassifyAddView(RestView):
    def post(self):
        """
        政策分类维护--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            policyclassify = PolicyClassify(policyName=request.form['policyName'])
            db.session.add(policyclassify)
        return "已发布", 200


class PolicyClassifyDeleteView(RestView):
    def post(self):
        """
        政策分类维护--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = PolicyClassify.query.filter(PolicyClassify.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class PolicyClassifyUpdateView(RestView):
    def post(self):
        """
        政策分类维护--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = PolicyClassify.query.filter(PolicyClassify.id == request.form['id']).first()
            result.policyName = request.form['policyName']
        return "已修改", 200


class PolicyClassifyView(RestView):
    def post(self):
        """
        政策分类维护--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        policyName = request.form['policyName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'policyName': policyName
            },
            'rows': PolicyClassify.query.filter(PolicyClassify.policyName.like('%' + policyName + '%'),
                                                PolicyClassify.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': PolicyClassify.query.filter(PolicyClassify.policyName.like('%' + policyName + '%'),
                                                 PolicyClassify.deleted == 0).count(),
            'totalPageCount': PolicyClassify.query.filter(PolicyClassify.policyName.like('%' + policyName + '%'),
                                                          PolicyClassify.deleted == 0).paginate(page=int(pageNum),
                                                                                                per_page=int(
                                                                                                    pageSize)).pages
        }
        content, errors = PolicyClassifySchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓产业园推荐
class IndustrialParkAddView(RestView):
    def post(self):
        """
        产业园推荐--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            industrialpark = IndustrialPark(industrialName=request.form['industrialName'], href=request.form['href'],
                                            sort=request.form['sort'], top=request.form['top'])
            db.session.add(industrialpark)
        return "已发布", 200


class IndustrialParkDeleteView(RestView):
    def post(self):
        """
        产业园推荐--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = IndustrialPark.query.filter(IndustrialPark.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class IndustrialParkUpdateView(RestView):
    def post(self):
        """
        产业园推荐--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = IndustrialPark.query.filter(IndustrialPark.id == request.form['id']).first()
            result.industrialName = request.form['industrialName']
            result.href = request.form['href']
            result.sort = request.form['sort']
            result.top = request.form['top']
        return "已修改", 200


class IndustrialParkView(RestView):
    def post(self):
        """
        产业园推荐--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        industrialName = request.form['industrialName']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'industrialName': industrialName
            },
            'rows': IndustrialPark.query.filter(IndustrialPark.industrialName.like('%' + industrialName + '%'),
                                                IndustrialPark.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': IndustrialPark.query.filter(IndustrialPark.industrialName.like('%' + industrialName + '%'),
                                                 IndustrialPark.deleted == 0).count(),
            'totalPageCount': IndustrialPark.query.filter(
                IndustrialPark.industrialName.like('%' + industrialName + '%'),
                IndustrialPark.deleted == 0).paginate(page=int(pageNum),
                                                      per_page=int(
                                                          pageSize)).pages
        }
        content, errors = IndustrialParkSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓示范基地管理

class BaseManageAddView(RestView):
    def post(self):
        """
        试验区管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            basemanage = BaseManage(baseName=request.form['baseName'], baseStyle=request.form['baseStyle'],
                                    baseBatc=request.form['baseBatc'], area=request.form['area'],
                                    policyUnit=request.form['policyUnit'], creator=request.form['creator'],
                                    createTime=datetime.strptime(request.form['createTime'], '%Y-%m-%d %H:%M:%S'),
                                    modifier=request.form['modifier'],
                                    modifyTime=datetime.strptime(request.form['modifyTime'],
                                                                 '%Y-%m-%d %H:%M:%S'),
                                    sort=request.form['sort'], top=request.form['top'])
            db.session.add(basemanage)
        return "已发布", 200


class BaseManageDeleteView(RestView):
    def post(self):
        """
        试验区管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = BaseManage.query.filter(BaseManage.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class BaseManageUpdateView(RestView):
    def post(self):
        """
        试验区管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = BaseManage.query.filter(BaseManage.id == request.form['id']).first()
            result.baseName = request.form['baseName']
            result.baseStyle = request.form['baseStyle']
            result.baseBatc = request.form['baseBatc']
            result.area = request.form['area']
            result.policyUnit = request.form['policyUnit']
            result.creator = request.form['creator']
            result.createTime = datetime.strptime(request.form['createTime'], '%Y-%m-%d %H:%M:%S')
            result.modifier = request.form['modifier']
            result.modifyTime = datetime.strptime(request.form['modifyTime'], '%Y-%m-%d %H:%M:%S')
            result.sort = request.form['sort']
            result.top = request.form['top']
        return "已修改", 200


class BaseManageView(RestView):
    def post(self):
        """
        试验区管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        baseStyle = request.form['baseStyle']
        baseBatc = request.form['baseBatc']
        baseName = request.form['baseName']
        top = request.form['top']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersNumberMap': {
                'baseStyle': baseStyle,
                'baseBatc': baseBatc,
                'top': top
            },
            'parametersStringMap': {
                'baseName': baseName
            },
            'rows': BaseManage.query.filter(BaseManage.baseStyle.like('%' + baseStyle + '%'),
                                            BaseManage.baseBatc.like('%' + baseBatc + '%'),
                                            BaseManage.baseName.like('%' + baseName + '%'),
                                            BaseManage.top.like('%' + top + '%'),
                                            BaseManage.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': BaseManage.query.filter(BaseManage.baseStyle.like('%' + baseStyle + '%'),
                                             BaseManage.baseBatc.like('%' + baseBatc + '%'),
                                             BaseManage.baseName.like('%' + baseName + '%'),
                                             BaseManage.top.like('%' + top + '%'),
                                             BaseManage.deleted == 0).count(),
            'totalPageCount': BaseManage.query.filter(BaseManage.baseStyle.like('%' + baseStyle + '%'),
                                                      BaseManage.baseBatc.like('%' + baseBatc + '%'),
                                                      BaseManage.baseName.like('%' + baseName + '%'),
                                                      BaseManage.top.like('%' + top + '%'),
                                                      BaseManage.deleted == 0).paginate(page=int(pageNum),
                                                                                        per_page=int(
                                                                                            pageSize)).pages
        }
        print(data)
        content, errors = BaseManageSchema().dump(data)
        print(content)
        print(errors)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓用户浏览信息
class UserBrowsingMessageView(RestView):
    def post(self):
        """
        用户浏览信息--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        bussinessType = request.form['bussinessType']
        userType = request.form['userType']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'bussinessType': bussinessType,
                'userType': userType
            },
            'rows': UserBrowsingMessage.query.filter(UserBrowsingMessage.bussinessType.like('%' + bussinessType + '%'),
                                                     UserBrowsingMessage.userType.like('%' + userType + '%'),
                                                     UserBrowsingMessage.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': UserBrowsingMessage.query.filter(UserBrowsingMessage.bussinessType.like('%' + bussinessType + '%'),
                                                      UserBrowsingMessage.userType.like('%' + userType + '%'),
                                                      UserBrowsingMessage.deleted == 0).count(),
            'totalPageCount': UserBrowsingMessage.query.filter(
                UserBrowsingMessage.bussinessType.like('%' + bussinessType + '%'),
                UserBrowsingMessage.userType.like('%' + userType + '%'),
                UserBrowsingMessage.deleted == 0).paginate(page=int(pageNum),
                                                           per_page=int(
                                                               pageSize)).pages
        }
        content, errors = UserBrowsingMessageSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓用户搜索信息
class UserSearchInfoView(RestView):
    def post(self):
        """
        用户搜索信息--查--搜索页面类型未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        userSearchContent = request.form['userSearchContent']
        userType = request.form['userType']
        userSearchMethod = request.form['userSearchMethod']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'userSearchContent': userSearchContent,
                'userType': userType,
                'userSearchMethod': userSearchMethod
            },
            'rows': UserSearchInfo.query.filter(UserSearchInfo.userSearchContent.like('%' + userSearchContent + '%'),
                                                UserSearchInfo.userType.like('%' + userType + '%'),
                                                UserSearchInfo.userSearchMethod.like('%' + userSearchMethod + '%'),
                                                UserSearchInfo.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': UserSearchInfo.query.filter(UserSearchInfo.userSearchContent.like('%' + userSearchContent + '%'),
                                                 UserSearchInfo.userType.like('%' + userType + '%'),
                                                 UserSearchInfo.userSearchMethod.like('%' + userSearchMethod + '%'),
                                                 UserSearchInfo.deleted == 0).count(),
            'totalPageCount': UserSearchInfo.query.filter(
                UserSearchInfo.userSearchContent.like('%' + userSearchContent + '%'),
                UserSearchInfo.userType.like('%' + userType + '%'),
                UserSearchInfo.userSearchMethod.like('%' + userSearchMethod + '%'),
                UserSearchInfo.deleted == 0).paginate(page=int(pageNum),
                                                      per_page=int(
                                                          pageSize)).pages
        }
        content, errors = UserSearchInfoSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓试验区管理
class PilotManagementAddView(RestView):
    def post(self):
        """
        试验区管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            pilotmanagement = PilotManagement(pilotName=request.form['pilotName'], creator=request.form['creator'],
                                              createTime=datetime.strptime(request.form['createTime'],
                                                                           '%Y-%m-%d %H:%M:%S'),
                                              modifier=request.form['modifier'],
                                              modifyTime=datetime.strptime(request.form['modifyTime'],
                                                                           '%Y-%m-%d %H:%M:%S'),
                                              sort=request.form['sort'], top=request.form['top'])
            db.session.add(pilotmanagement)
        return "已发布", 200


class PilotManagementDeleteView(RestView):
    def post(self):
        """
        试验区管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = PilotManagement.query.filter(PilotManagement.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class PilotManagementUpdateView(RestView):
    def post(self):
        """
        试验区管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = PilotManagement.query.filter(PilotManagement.id == request.form['id']).first()
            result.pilotName = request.form['pilotName']
            result.creator = request.form['creator']
            result.createTime = datetime.strptime(request.form['createTime'], '%Y-%m-%d %H:%M:%S')
            result.modifier = request.form['modifier']
            result.modifyTime = datetime.strptime(request.form['modifyTime'], '%Y-%m-%d %H:%M:%S')
            result.sort = request.form['sort']
            result.top = request.form['top']
        return "已修改", 200


class PilotManagementView(RestView):
    def post(self):
        """
        试验区管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        pilotName = request.form['pilotName']
        top = request.form['top']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersNumberMap': {
                'top': top
            },
            'parametersStringMap': {
                'pilotName': pilotName
            },
            'rows': PilotManagement.query.filter(PilotManagement.pilotName.like('%' + pilotName + '%'),
                                                 PilotManagement.top.like('%' + top + '%'),
                                                 PilotManagement.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': PilotManagement.query.filter(PilotManagement.pilotName.like('%' + pilotName + '%'),
                                                  PilotManagement.top.like('%' + top + '%'),
                                                  PilotManagement.deleted == 0).count(),
            'totalPageCount': PilotManagement.query.filter(PilotManagement.pilotName.like('%' + pilotName + '%'),
                                                           PilotManagement.top.like(
                                                               '%' + top + '%'),
                                                           PilotManagement.deleted == 0).paginate(page=int(pageNum),
                                                                                                  per_page=int(
                                                                                                      pageSize)).pages
        }
        print(data['rows'][0])
        content, errors = PilotManagementSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓建言献策
class SuggestionsDeleteView(RestView):
    def post(self):
        """
    建言献策--减
    @ author: lyfy
    :return:
    ---
    tags:
      - 后台页面
    """
        with db.auto_commit():
            result = Suggestions.query.filter(Suggestions.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class SuggestionsView(RestView):
    def post(self):
        """
    建言献策--查
    @ author: lyfy
    :return:
    ---
    tags:
      - 后台页面
    """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        status = request.form['status']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'status': status
            },
            'rows': Suggestions.query.filter(Suggestions.status.like('%' + status + '%'),
                                             Suggestions.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': Suggestions.query.filter(Suggestions.status.like('%' + status + '%'),
                                              Suggestions.deleted == 0).count(),
            'totalPageCount': Suggestions.query.filter(Suggestions.status.like('%' + status + '%'),
                                                       Suggestions.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).pages
        }
        content, errors = SuggestionsSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓政策统计
class PolicyStatisticsView(RestView):
    def post(self):
        """
        政策统计
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title
            },
            'rows': PolicyStatistics.query.filter(PolicyStatistics.title.like('%' + title + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': PolicyStatistics.query.filter(PolicyStatistics.title.like('%' + title + '%')).count(),
            'totalPageCount': PolicyStatistics.query.filter(PolicyStatistics.title.like('%' + title + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).pages
        }
        content, errors = PolicyStatisticsSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓日志管理--系统日志管理
class JournalSystemView(RestView):
    def post(self):
        """
        系统日志管理-----时间筛选未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        operationtype = request.form['operationtype']
        operator = request.form['operator']
        starttime = int(time.mktime(time.strptime(request.form['starttime'], "%Y-%m-%d")))
        endtime = int(time.mktime(time.strptime(request.form['endtime'], "%Y-%m-%d")))
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'operationtype': operationtype,
                'operator': operator,
                'starttime': starttime,
                'endtime': endtime
            },
            'rows': JournalSystem.query.filter(JournalSystem.operationtype.like('%' + operationtype + '%'),
                                               JournalSystem.operator.like('%' + operator + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': JournalSystem.query.filter(JournalSystem.operationtype.like('%' + operationtype + '%'),
                                                JournalSystem.operator.like('%' + operator + '%')).count(),
            'totalPageCount': JournalSystem.query.filter(JournalSystem.operationtype.like('%' + operationtype + '%'),
                                                         JournalSystem.operator.like('%' + operator + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).pages
        }
        print(data)
        content, errors = JournalSystemSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓日志管理--政策日志管理
class JournalPolicyView(RestView):
    def post(self):
        """
        政策管理-----时间筛选未完成，模块名称筛选未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        type = request.form['type']
        starttime = int(time.mktime(time.strptime(request.form['starttime'], "%Y-%m-%d")))
        endtime = int(time.mktime(time.strptime(request.form['endtime'], "%Y-%m-%d")))
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'type': type,
                'starttime': starttime,
                'endtime': endtime
            },
            'rows': JournalPolicy.query.filter(JournalPolicy.type.like('%' + type + '%')).paginate(page=int(pageNum),
                                                                                                   per_page=int(
                                                                                                       pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': JournalPolicy.query.filter(JournalPolicy.type.like('%' + type + '%')).count(),
            'totalPageCount': JournalPolicy.query.filter(JournalPolicy.type.like('%' + type + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).pages
        }
        print(data)
        content, errors = JournalPolicySchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓关于我们
class AboutUsView(RestView):
    def post(self):
        """
        关于我们
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'rows': AboutUs.query.filter_by(deleted=0).paginate(page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': AboutUs.query.filter_by(deleted=0).count(),
            'totalPageCount': AboutUs.query.filter_by(deleted=0).paginate(page=int(pageNum),
                                                                          per_page=int(pageSize)).pages
        }
        content, errors = AboutUsSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓移动端功能管理--报告管理
class MovePresentationAddView(RestView):
    def post(self):
        """
        移动端功能管理--报告管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            movepresentation = MovePresentation(title=request.form['title'], description=request.form['description'],
                                                company=request.form['company'],
                                                publisher=request.form['publisher'],
                                                publishtime=datetime.strptime(request.form['publishtime'], '%Y-%m-%d'),
                                                creationtime=datetime.strptime(request.form['creationtime'],
                                                                               '%Y-%m-%d %H:%M:%S'),
                                                modifier=request.form['modifier'],
                                                mtime=datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S'),
                                                sort=request.form['sort'], releaselogo=request.form['releaselogo'])
            db.session.add(movepresentation)
        return "已发布", 200


class MovePresentationDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--报告管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MovePresentation.query.filter(MovePresentation.id == request.form['id']).first()
            # db.session.delete(result)
            result.deleted = 1
        return "已删除", 200


class MovePresentationUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--报告管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MovePresentation.query.filter(MovePresentation.id == request.form['id']).first()
            result.title = request.form['title']
            result.description = request.form['description']
            result.company = request.form['company']
            result.publisher = request.form['publisher']
            result.publishtime = datetime.strptime(request.form['publishtime'], '%Y-%m-%d')
            result.creationtime = datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S')
            result.modifier = request.form['modifier']
            result.mtime = datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S')
            result.sort = request.form['sort']
            result.releaselogo = request.form['releaselogo']
        return "已修改", 200


class MovePresentationView(RestView):
    def post(self):
        """
        移动端功能管理--报告管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        releaselogo = request.form['releaselogo']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
                'releaselogo': releaselogo
            },
            'rows': MovePresentation.query.filter(MovePresentation.title.like('%' + title + '%'),
                                                  MovePresentation.releaselogo.like('%' + releaselogo + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': MovePresentation.query.filter(MovePresentation.title.like('%' + title + '%'),
                                                   MovePresentation.releaselogo.like('%' + releaselogo + '%')).count(),
            'totalPageCount': MovePresentation.query.filter(MovePresentation.title.like('%' + title + '%'),
                                                            MovePresentation.releaselogo.like(
                                                                '%' + releaselogo + '%')).paginate(page=int(pageNum),
                                                                                                   per_page=int(
                                                                                                       pageSize)).pages
        }
        content, errors = MovePresentationSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓移动端功能管理--服务管理
class MoveServiceAddView(RestView):
    def post(self):
        """
        移动端功能管理--服务管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            moveservice = MoveService(title=request.form['title'], description=request.form['description'],
                                      founder=request.form['founder'],
                                      creationtime=datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S'),
                                      modifier=request.form['modifier'],
                                      mtime=datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S'),
                                      sort=request.form['sort'])
            db.session.add(moveservice)
        return "已发布", 200


class MoveServiceDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--服务管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveService.query.filter(MoveService.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class MoveServiceUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--服务管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveService.query.filter(MoveService.id == request.form['id']).first()
            result.title = request.form['title']
            result.description = request.form['description']
            result.founder = request.form['founder']
            result.creationtime = datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S')
            result.modifier = request.form['modifier']
            result.mtime = datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S')
            result.sort = request.form['sort']
        return "已修改", 200


class MoveServiceView(RestView):
    def post(self):
        """
        移动端功能管理--服务管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
            },
            'rows': MoveService.query.filter(MoveService.title.like('%' + title + '%')).paginate(page=int(pageNum),
                                                                                                 per_page=int(
                                                                                                     pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': MoveService.query.filter(MoveService.title.like('%' + title + '%')).count(),
            'totalPageCount': MoveService.query.filter(MoveService.title.like('%' + title + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).pages
        }
        content, errors = MoveServiceSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓移动端功能管理--活动首页管理
class MoveHomePageAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            movehomepage = MoveHomePage(title=request.form['title'], description=request.form['description'],
                                        founder=request.form['founder'],
                                        creationtime=datetime.strptime(request.form['creationtime'],
                                                                       '%Y-%m-%d %H:%M:%S'),
                                        modifier=request.form['modifier'],
                                        mtime=datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S'),
                                        sort=request.form['sort'])
            db.session.add(movehomepage)
        return "已发布", 200


class MoveHomePageDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveHomePage.query.filter(MoveHomePage.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class MoveHomePageUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveHomePage.query.filter(MoveHomePage.id == request.form['id']).first()
            result.title = request.form['title']
            result.description = request.form['description']
            result.founder = request.form['founder']
            result.creationtime = datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S')
            result.modifier = request.form['modifier']
            result.mtime = datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S')
            result.sort = request.form['sort']
        return "已修改", 200


class MoveHomePageView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
            },
            'rows': MoveHomePage.query.filter(MoveHomePage.title.like('%' + title + '%')).paginate(page=int(pageNum),
                                                                                                   per_page=int(
                                                                                                       pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': MoveHomePage.query.filter(MoveHomePage.title.like('%' + title + '%')).count(),
            'totalPageCount': MoveHomePage.query.filter(MoveHomePage.title.like('%' + title + '%')).paginate(
                page=int(pageNum), per_page=int(pageSize)).pages
        }
        content, errors = MoveHomePageSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓移动端功能管理--版本管理
class MoveVersionAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            moveversion = MoveVersion(number=request.form['number'], information=request.form['information'],
                                      classification=request.form['classification'],
                                      compulsoryrenewal=request.form['compulsoryrenewal'],
                                      founder=request.form['founder'],
                                      creationtime=datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S'),
                                      modifier=request.form['modifier'],
                                      mtime=datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S'))
            db.session.add(moveversion)
        return "已发布", 200


class MoveVersionDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveVersion.query.filter(MoveVersion.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class MoveVersionUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveVersion.query.filter(MoveVersion.id == request.form['id'], MoveVersion.deleted == 0).first()
            result.number = request.form['number']
            result.information = request.form['information']
            result.classification = request.form['classification']
            result.compulsoryrenewal = request.form['compulsoryrenewal']
            result.founder = request.form['founder']
            result.creationtime = datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S')
            result.modifier = request.form['modifier']
            result.mtime = datetime.strptime(request.form['mtime'], '%Y-%m-%d %H:%M:%S')
        return "已修改", 200


class MoveVersionView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        number = request.form['number']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'number': number,
            },
            'rows': MoveVersion.query.filter(MoveVersion.number.like('%' + number + '%'),
                                             MoveVersion.deleted == 0).paginate(page=int(pageNum),
                                                                                per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': MoveVersion.query.filter(MoveVersion.number.like('%' + number + '%'),
                                              MoveVersion.deleted == 0).count(),
            'totalPageCount': MoveVersion.query.filter(MoveVersion.number.like('%' + number + '%'),
                                                       MoveVersion.deleted == 0).paginate(page=int(pageNum),
                                                                                          per_page=int(pageSize)).pages
        }
        content, errors = MoveVersionSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓移动端功能管理--用户管理

class MoveUserDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveUser.query.filter(MoveUser.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class MoveUserView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        phone = request.form['phone']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'phone': phone,
            },
            'rows': MoveUser.query.filter(MoveUser.phone.like('%' + phone + '%'), MoveUser.deleted == 0).paginate(
                page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': MoveUser.query.filter(MoveUser.phone.like('%' + phone + '%'), MoveUser.deleted == 0).count(),
            'totalPageCount': MoveUser.query.filter(MoveUser.phone.like('%' + phone + '%'),
                                                    MoveUser.deleted == 0).paginate(page=int(pageNum),
                                                                                    per_page=int(pageSize)).pages
        }
        content, errors = MoveUserSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓移动端功能管理--简报管理

class MoveBriefingAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            movebriefing = MoveBriefing(title=request.form['title'],
                                        time=datetime.strptime(request.form['time'], '%Y-%m-%d'),
                                        releaselogo=request.form['releaselogo'])
            db.session.add(movebriefing)
        return "已发布", 200


class MoveBriefingDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveBriefing.query.filter(MoveBriefing.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class MoveBriefingUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = MoveBriefing.query.filter(MoveBriefing.id == request.form['id'], MoveBriefing.deleted == 0).first()
            result.title = request.form['title']
            result.time = datetime.strptime(request.form['time'], '%Y-%m-%d')
            result.releaselogo = request.form['releaselogo']
        return "已修改", 200


class MoveBriefingView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查--时间搜素未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        releaselogo = request.form['releaselogo']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
                'releaselogo': releaselogo
            },
            'rows': MoveBriefing.query.filter(MoveBriefing.title.like('%' + title + '%'),
                                              MoveBriefing.releaselogo.like('%' + releaselogo + '%'),
                                              MoveBriefing.deleted == 0).paginate(page=int(pageNum),
                                                                                  per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': MoveBriefing.query.filter(MoveBriefing.title.like('%' + title + '%'),
                                               MoveBriefing.releaselogo.like('%' + releaselogo + '%'),
                                               MoveBriefing.deleted == 0).count(),
            'totalPageCount': MoveBriefing.query.filter(MoveBriefing.title.like('%' + title + '%'),
                                                        MoveBriefing.releaselogo.like('%' + releaselogo + '%'),
                                                        MoveBriefing.deleted == 0).paginate(page=int(pageNum),
                                                                                            per_page=int(
                                                                                                pageSize)).pages
        }
        content, errors = MoveBriefingSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓服务拓展--办事指南管理
class GuideToAffairsAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            guidetoaffairs = GuideToAffairs(title=request.form['title'],
                                            description=request.form['description'],
                                            source=request.form['source'],
                                            publishtime=datetime.strptime(request.form['publishtime'], '%Y-%m-%d'),
                                            creationtime=datetime.strptime(request.form['creationtime'],
                                                                           '%Y-%m-%d %H:%M:%S'),
                                            founder=request.form['founder'],
                                            renewing=request.form['renewing'],
                                            updatatime=datetime.strptime(request.form['updatatime'],
                                                                         '%Y-%m-%d %H:%M:%S'),
                                            releaselogo=request.form['releaselogo'])
            db.session.add(guidetoaffairs)
        return "已发布", 200


class GuideToAffairsDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = GuideToAffairs.query.filter(GuideToAffairs.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class GuideToAffairsUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = GuideToAffairs.query.filter(GuideToAffairs.id == request.form['id'],
                                                 GuideToAffairs.deleted == 0).first()
            result.title = request.form['title']
            result.description = request.form['description']
            result.source = request.form['source']
            result.publishtime = datetime.strptime(request.form['publishtime'], '%Y-%m-%d')
            result.creationtime = datetime.strptime(request.form['creationtime'], '%Y-%m-%d %H:%M:%S')
            result.founder = request.form['founder']
            result.renewing = request.form['renewing']
            result.updatatime = datetime.strptime(request.form['updatatime'], '%Y-%m-%d %H:%M:%S')
            result.releaselogo = request.form['releaselogo']
        return "已修改", 200


class GuideToAffairsView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查--时间搜素未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title
            },
            'rows': GuideToAffairs.query.filter(GuideToAffairs.title.like('%' + title + '%'),
                                                GuideToAffairs.deleted == 0).paginate(page=int(pageNum),
                                                                                      per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': GuideToAffairs.query.filter(GuideToAffairs.title.like('%' + title + '%'),
                                                 GuideToAffairs.deleted == 0).count(),
            'totalPageCount': GuideToAffairs.query.filter(GuideToAffairs.title.like('%' + title + '%'),
                                                          GuideToAffairs.deleted == 0).paginate(page=int(pageNum),
                                                                                                per_page=int(
                                                                                                    pageSize)).pages
        }
        content, errors = GuideToAffairsSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓服务拓展--政府性基金和行政事业型收费

class GovernmentFundsAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            governmentfunds = GovernmentFunds(title=request.form['title'],
                                              costcategory=request.form['costcategory'],
                                              publisher=request.form['publisher'],
                                              publishtime=datetime.strptime(request.form['publishtime'],
                                                                            '%Y-%m-%d %H:%M:%S'),
                                              renewing=request.form['renewing'],
                                              updatatime=datetime.strptime(request.form['updatatime'],
                                                                           '%Y-%m-%d %H:%M:%S'),
                                              releaselogo=request.form['releaselogo'])
            db.session.add(governmentfunds)
        return "已发布", 200


class GovernmentFundsDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = GovernmentFunds.query.filter(GovernmentFunds.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class GovernmentFundsUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = GovernmentFunds.query.filter(GovernmentFunds.id == request.form['id'],
                                                  GovernmentFunds.deleted == 0).first()
            result.title = request.form['title']
            result.costcategory = request.form['costcategory']
            result.publisher = request.form['publisher']
            result.publishtime = datetime.strptime(request.form['publishtime'], '%Y-%m-%d %H:%M:%S')
            result.renewing = request.form['renewing']
            result.updatatime = datetime.strptime(request.form['updatatime'], '%Y-%m-%d %H:%M:%S')
            result.releaselogo = request.form['releaselogo']
        return "已修改", 200


class GovernmentFundsView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查--时间搜素未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        costcategory = request.form['costcategory']
        releaselogo = request.form['releaselogo']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
                'costcategory': costcategory,
                'releaselogo': releaselogo
            },
            'rows': GovernmentFunds.query.filter(GovernmentFunds.title.like('%' + title + '%'),
                                                 GovernmentFunds.costcategory.like('%' + costcategory + '%'),
                                                 GovernmentFunds.releaselogo.like('%' + releaselogo + '%'),
                                                 GovernmentFunds.deleted == 0).paginate(page=int(pageNum),
                                                                                        per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': GovernmentFunds.query.filter(GovernmentFunds.title.like('%' + title + '%'),
                                                  GovernmentFunds.costcategory.like('%' + costcategory + '%'),
                                                  GovernmentFunds.releaselogo.like('%' + releaselogo + '%'),
                                                  GovernmentFunds.deleted == 0).count(),
            'totalPageCount': GovernmentFunds.query.filter(GovernmentFunds.title.like('%' + title + '%'),
                                                           GovernmentFunds.costcategory.like('%' + costcategory + '%'),
                                                           GovernmentFunds.releaselogo.like('%' + releaselogo + '%'),
                                                           GovernmentFunds.deleted == 0).paginate(page=int(pageNum),
                                                                                                  per_page=int(
                                                                                                      pageSize)).pages
        }
        content, errors = GovernmentFundsSchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓服务拓展--双创税收优惠政策查询
class FavouredPolicyAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            favouredpolicy = FavouredPolicy(title=request.form['title'],
                                            taxstage=request.form['taxstage'],
                                            taxcategory=request.form['taxcategory'],
                                            publisher=request.form['publisher'],
                                            publishtime=datetime.strptime(request.form['publishtime'],
                                                                          '%Y-%m-%d %H:%M:%S'),
                                            renewing=request.form['renewing'],
                                            updatatime=datetime.strptime(request.form['updatatime'],
                                                                         '%Y-%m-%d %H:%M:%S'),
                                            releaselogo=request.form['releaselogo'])
            db.session.add(favouredpolicy)
        return "已发布", 200


class FavouredPolicyDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = FavouredPolicy.query.filter(FavouredPolicy.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class FavouredPolicyUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = FavouredPolicy.query.filter(FavouredPolicy.id == request.form['id'],
                                                 FavouredPolicy.deleted == 0).first()
            result.title = request.form['title']
            result.taxstage = request.form['taxstage']
            result.taxcategory = request.form['taxcategory']
            result.publisher = request.form['publisher']
            result.publishtime = datetime.strptime(request.form['publishtime'], '%Y-%m-%d %H:%M:%S')
            result.renewing = request.form['renewing']
            result.updatatime = datetime.strptime(request.form['updatatime'], '%Y-%m-%d %H:%M:%S')
            result.releaselogo = request.form['releaselogo']
        return "已修改", 200


class FavouredPolicyView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查--时间搜素未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        title = request.form['title']
        taxcategory = request.form['taxcategory']
        releaselogo = request.form['releaselogo']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'title': title,
                'taxcategory': taxcategory,
                'releaselogo': releaselogo
            },
            'rows': FavouredPolicy.query.filter(FavouredPolicy.title.like('%' + title + '%'),
                                                FavouredPolicy.taxcategory.like('%' + taxcategory + '%'),
                                                FavouredPolicy.releaselogo.like('%' + releaselogo + '%'),
                                                FavouredPolicy.deleted == 0).paginate(page=int(pageNum),
                                                                                      per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': FavouredPolicy.query.filter(FavouredPolicy.title.like('%' + title + '%'),
                                                 FavouredPolicy.taxcategory.like('%' + taxcategory + '%'),
                                                 FavouredPolicy.releaselogo.like('%' + releaselogo + '%'),
                                                 FavouredPolicy.deleted == 0).count(),
            'totalPageCount': FavouredPolicy.query.filter(FavouredPolicy.title.like('%' + title + '%'),
                                                          FavouredPolicy.taxcategory.like('%' + taxcategory + '%'),
                                                          FavouredPolicy.releaselogo.like('%' + releaselogo + '%'),
                                                          FavouredPolicy.deleted == 0).paginate(page=int(pageNum),
                                                                                                per_page=int(
                                                                                                    pageSize)).pages
        }
        content, errors = FavouredPolicySchema().dump(data)
        if errors:
            return errors, 400
        return content


# ↓↓↓↓↓↓服务拓展--取消和下放的行政事项
class CancellationAndDecentralizationAddView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--增加
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            cancellationanddecentralization = CancellationAndDecentralization(name=request.form['name'],
                                                                              itemtype=request.form['itemtype'],
                                                                              department=request.form['department'],
                                                                              publisher=request.form['publisher'],
                                                                              publishtime=datetime.strptime(
                                                                                  request.form['publishtime'],
                                                                                  '%Y-%m-%d %H:%M:%S'),
                                                                              renewing=request.form['renewing'],
                                                                              updatatime=datetime.strptime(
                                                                                  request.form['updatatime'],
                                                                                  '%Y-%m-%d %H:%M:%S'),
                                                                              releaselogo=request.form['releaselogo'])
            db.session.add(cancellationanddecentralization)
        return "已发布", 200


class CancellationAndDecentralizationDeleteView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--删除
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = CancellationAndDecentralization.query.filter(
                CancellationAndDecentralization.id == request.form['id']).first()
            result.deleted = 1
        return "已删除", 200


class CancellationAndDecentralizationUpdateView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--改
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        with db.auto_commit():
            result = CancellationAndDecentralization.query.filter(
                CancellationAndDecentralization.id == request.form['id'],
                CancellationAndDecentralization.deleted == 0).first()
            result.name = request.form['name']
            result.itemtype = request.form['itemtype']
            result.department = request.form['department']
            result.publisher = request.form['publisher']
            result.publishtime = datetime.strptime(request.form['publishtime'], '%Y-%m-%d %H:%M:%S')
            result.renewing = request.form['renewing']
            result.updatatime = datetime.strptime(request.form['updatatime'], '%Y-%m-%d %H:%M:%S')
            result.releaselogo = request.form['releaselogo']
        return "已修改", 200


class CancellationAndDecentralizationView(RestView):
    def post(self):
        """
        移动端功能管理--活动首页管理--查--时间搜素未完成
        @ author：lyfy
        :return:
        ---
        tags:
          - 后台页面
        """
        pageNum = request.form['pageNum']
        pageSize = request.form['pageSize']
        name = request.form['name']
        releaselogo = request.form['releaselogo']
        data = {
            'colmodel': [],
            'limit': int(pageSize),
            'parametersStringMap': {
                'name': name,
                'releaselogo': releaselogo
            },
            'rows': CancellationAndDecentralization.query.filter(
                CancellationAndDecentralization.name.like('%' + name + '%'),
                CancellationAndDecentralization.releaselogo.like('%' + releaselogo + '%'),
                CancellationAndDecentralization.deleted == 0).paginate(page=int(pageNum), per_page=int(pageSize)).items,
            'start': (int(pageNum) - 1) * 10,
            'total': CancellationAndDecentralization.query.filter(
                CancellationAndDecentralization.name.like('%' + name + '%'),
                CancellationAndDecentralization.releaselogo.like('%' + releaselogo + '%'),
                CancellationAndDecentralization.deleted == 0).count(),
            'totalPageCount': CancellationAndDecentralization.query.filter(
                CancellationAndDecentralization.name.like('%' + name + '%'),
                CancellationAndDecentralization.releaselogo.like('%' + releaselogo + '%'),
                CancellationAndDecentralization.deleted == 0).paginate(page=int(pageNum), per_page=int(pageSize)).pages
        }
        content, errors = CancellationAndDecentralizationSchema().dump(data)
        if errors:
            return errors, 400
        return content
