# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-02
import os
from flask import (Flask,request....)
"""
from marshmallow import (Schema as _Schema, fields, validate)

__all__ = ['CmemberSchema', 'LocalSchema', 'SocioGroupSchema', 'LpolicySchema',
           'BaseCitySchema', 'PanalysisSchema', 'AtrackingSchema', 'ScolumnSchema',
           'BroadcastSchema', 'DongTaiListSchema', "ScolumnListSchema", "NewDepartureListSchema",
           'PolicyAnalysisListSchema', 'ActivitytrackingListSchema', 'ServiceExpansionSchema', 'PolicyStatisticsSchema',
           'JournalSystemSchema', 'JournalPolicySchema', 'AboutUsSchema', 'MovePresentationSchema',
           'MoveServiceSchema', 'MoveHomePageSchema', 'MoveVersionSchema', 'MoveUserSchema',
           'MoveBriefingSchema', 'GuideToAffairsSchema', 'GovernmentFundsSchema', 'FavouredPolicySchema',
           'CancellationAndDecentralizationSchema', 'SuggestionsSchema', 'PilotManagementSchema',
           'UserSearchInfoSchema',
           'UserBrowsingMessageSchema', 'BaseManageSchema', 'IndustrialParkSchema', 'PolicyClassifySchema',
           'SubjectClassificationSchema', 'AreaServiceSchema', 'BusinessServiceSchema', 'TimerShaftSchema',
           'EcosphereSchema', 'PolicyReleaseSchema']


class Schema(_Schema):
    """
    继承Schema类，创建Schema1类
    author lyfy
    :return:{Id ， imagePaths，title，insertTime，pubtime，shortContent，source}
    """
    id = fields.Integer(dump_only=True)
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    insertTime = fields.DateTime(dump_only=True)
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)


class Schema_one(_Schema):
    """
    继承Schema类，创建Schema2类
    author lyfy
    :return:{Id ，title}
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)


class CmemberSchema(Schema):
    """
    部委
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class LocalSchema(Schema):
    """
    地方
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent,source,title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class SocioGroupSchema(Schema):
    """
    社会团体
    author:lyfy
    :return:Id,imagePaths,insertTime,pubtime,shortContent,source,title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class BaseCitySchema(Schema):
    """
    基地
    author:lyfy
    :return:Id，imagePaths，insertTime，pubtime，shortContent，source，title
    """
    data = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)


class LpolicySchema(Schema_one):
    """
    最新政策
    author:lyfy
    :return:Id，pubTime，shortContent，source，titile
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(required=True)
    source = fields.String(required=True)
    issuedtime = fields.DateTime(dump_only=True)
    issuedno = fields.String(required=True)
    type1 = fields.Integer(required=True)
    link = fields.String(required=True)
    data = fields.Nested('self',
                         only=['id', 'title', 'pubtime', 'shortContent', 'issuedtime', 'issuedno', 'type1', 'link'],
                         many=True)


class PanalysisSchema(_Schema):
    """
    政策分析
    author:lyfy
    :return:businessId，title
    """
    businessId = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    type = fields.Integer(required=True)
    code = fields.Integer(requeired=True)
    msg = fields.String(requeired=True)
    # data = fields.Nested('self', only=["businessId", "title", "type"], many=True)
    data = fields.Nested("self", only=["businessId", "title", "type"], many=True)


class AtrackingSchema(Schema_one):
    """
    活动跟踪
    author:lyfy
    :return:Category，id，picPath，publishTime，source，title
    """
    # picPath = fields.String(validate=validate.Length(6, 12), required=True)
    # publishTime = fields.DateTime(dump_only=True)
    # source = fields.String(validate=validate.Length(6, 12), required=True)
    # category = fields.String(validate=validate.Length(6, 12), required=True)

    data = fields.Nested('self', only=["id", "title", "picPath", "publishTime", "source", "category"], many=True)


class ScolumnSchema(Schema_one):
    """
    专题专栏
    author:lyfy
    :return:Id，title
    """
    type = fields.Integer(required=True)
    category = fields.Integer(required=True)
    data = fields.Nested('self', only=["id", "title", "type", "category"], many=True)


class BroadcastSchema(Schema_one):
    """"
    轮播图
    author:lyfy
    :return:Id，title，imagepaths
    """
    imagePaths = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self', only=["id", "title", "imagePaths"], many=True)


class DongTaiListDataSchema(_Schema):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    # list = fields.List(fields.Field())
    list = fields.Nested('self', only=["id", "imagePaths", "title", "insertTime", "pubtime", "shortContent", "source"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class DongTaiListSchema(Schema):
    """
    动态列表
    author:lyfy
    :return:Id ， imagePaths，title，insertTime，pubtime，shortContent，source
    """
    # data = fields.Nested('self',only={"id","imagePaths","title","insertTime","pubtime","shortContent","source"},many=True)
    data = fields.Nested(DongTaiListDataSchema())


class AllNewGaiListDataSchema(Schema_one):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    # list = fields.List(fields.Field())
    list = fields.Nested('self', only=["id", "title", "category", "type"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class ScolumnListSchema(Schema):
    """"
    专题专栏列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested(AllNewGaiListDataSchema())


class NewDepartureListDataSchema(_Schema):
    data = fields.String(required=True)
    allCounts = fields.Integer(dump_only=True)
    currentPage = fields.Integer(dump_only=True)
    list = fields.Nested('self',
                         only=["id", "title", "pubtime", "shortContent", "source", "issuedno", "issuedtime", "link"],
                         many=True)
    pageCounts = fields.Integer(dump_only=True)
    pageSize = fields.Integer(dump_only=True)


class NewDepartureListSchema(Schema_one):
    """"
    最新政策列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested(NewDepartureListDataSchema())


class PolicyAnalysisListSchema(Schema_one):
    """"
    政策分析列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested('self', only=["businessId", "title"], many=True)


class ActivitytrackingListSchema(Schema_one):
    """"
    政策分析列表
    author:lyfy
    :return:Id，title,category,pubTime
    """
    data = fields.Nested('self', only=["id", "title", "picPath", "publishTime", "source", "category"], many=True)


class ServiceExpansionSchema(Schema_one):
    """
    服务拓展列表
    @author:lyfy
    :return:
    """
    pubtime = fields.DateTime(dump_only=True)
    shortContent = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    data = fields.Nested('self', only=['id', 'title', 'pubtime', 'shortContent', 'source'], many=True)


# ↓↓↓↓↓↓后台


class OmanagementSchema(Schema):
    """
    机构管理
    """
    Onumber = fields.String(validate=validate.Length(6, 12), required=True)
    Nauthority = fields.String(required=True)
    Oname = fields.String(required=True)
    Iabbreviation = fields.String(required=True)
    Iaddress = fields.String(required=True)
    Imailbox = fields.String(required=True)
    OWebsite = fields.String(required=True)
    Cnumber = fields.String(required=True)
    Mdescription = fields.String(required=True)


class RmanagementSchema(Schema):
    """
    角色管理
    """
    Rename = fields.String(required=True)
    Rdescription = fields.String(required=True)


class UmanagementSchema(Schema):
    """
    用户管理
    """
    Ainstitutions = fields.String(required=True)
    Theinstitution = fields.String(required=True)
    Uname = fields.String(required=True)
    Rname = fields.String(required=True)
    IDnumber = fields.String(required=True)
    DBirth = fields.String(required=True)
    Sex = fields.String(required=True)
    Mphone = fields.String(required=True)
    Wphone = fields.String(required=True)
    mailbox = fields.String(required=True)
    Wlock = fields.String(required=True)
    Dregistration = fields.String(required=True)


class BPmanagementSchema(Schema):
    """
    banner图片管理
    """
    Name = fields.String(required=True)
    Type = fields.String(required=True)
    link = fields.String(required=True)
    publisher = fields.String(required=True)
    Rtime = fields.DateTime(dump_only=True)
    Modifier = fields.String(required=True)
    Mtime = fields.String(required=True)
    sort = fields.Integer(required=True)
    settop = fields.String(required=True)


class MgroupSchema(Schema):
    """
    创业群体维护
    """
    Negroup = fields.String(required=True)
    Aperson = fields.String(required=True)
    Atime = fields.String(required=True)
    Modifier = fields.String(required=True)
    Mtime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    settop = fields.String(required=True)


class DmanagementSchema(Schema):
    """
    动态管理
    """
    title = fields.String(required=True)
    bintroduction = fields.String(required=True)
    Runit = fields.String(required=True)
    Rtime = fields.DateTime(required=True, dump_only=True)
    Ctime = fields.DateTime(dump_only=True)
    sort = fields.Integer(required=True)
    Rlogo = fields.String(required=True)
    settop = fields.String(required=True)
    Lmarkers = fields.String(required=True)


class PromanagementSchema(Schema):
    """
    宣传位管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    describe = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class FmanagementSchema(Schema):
    """
    金融资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class bmanagementSchema(Schema):
    """
    金融机构管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    sort = fields.String(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class TmanagementShema(Schema):
    """
    技术资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class MinstitutionsSchema(Schema):
    """
    技术机构管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class TimanagementSchema(Schema):
    """
    人才资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class TamanagementSchema(Schema):
    """
    人才机构管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class SitemanagementSchema(Schema):
    """
    场地资讯管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    sort = fields.Integer(required=True)
    category = fields.String(required=True)
    settop = fields.String(required=True)


class positionmanagementSchema(Schema):
    """
    宣传位管理
    """
    Name = fields.String(required=True)
    link = fields.String(required=True)
    Route = fields.String(required=True)
    Insertuser = fields.String(required=True)
    Insertiontime = fields.DateTime(dump_only=True)
    Updateuser = fields.String(required=True)
    utime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    settop = fields.String(required=True)


class AmanagementSchema(Schema):
    """
    成果展示管理
    """
    title = fields.String(required=True)
    Rtime = fields.DateTime(required=True)
    Ctime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    Rlogo = fields.String(required=True)
    settop = fields.String(required=True)


class MediamanageSchema(Schema):
    """
    媒体管理
    """
    meidaName = fields.String(required=True)
    businessType = fields.String(required=True)
    mediaType = fields.String(required=True)
    href = fields.String(required=True)
    top = fields.String(required=True)


class ActivityManageSchema(Schema):
    """
    活动管理
    """
    activityTitle = fields.String(required=True)
    activityType = fields.String(required=True)
    area = fields.String(required=True)
    activity = fields.String(required=True)
    releaseUnit = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    source = fields.String(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)


class MascotSchema(Schema):
    """
    吉祥物管理
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)


class GuestSchema(Schema):
    """
    嘉宾管理
    """
    title = fields.String(required=True)
    activityType = fields.String(required=True)
    publisher = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)


class HallSchema(Schema):
    """
    展厅管理
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)


class ActivityTypeSchema(Schema):
    """
    活动类别管理
    """
    activityTitle = fields.String(required=True)
    activityType = fields.String(required=True)
    activityIntro = fields.String(required=True)
    releasePeople = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    modifier = fields.String(required=True)
    updateTime = fields.DateTime(required=True)
    status = fields.String(required=True)
    pageView = fields.Integer(required=True)
    href = fields.String(required=True)


class CenterNewSchema(Schema):
    """
    中央快讯
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    Rtime = fields.DateTime(required=True)
    Mtime = fields.DateTime(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    releaseNote = fields.String(required=True)
    top = fields.String(required=True)
    source = fields.String(required=True)


class DepartmentSchema(Schema):
    """
    部委讯息
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    releaseNote = fields.String(required=True)
    top = fields.String(required=True)
    source = fields.String(required=True)


class policySchema(Schema):
    """
    政策讯息
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    mkdirTime = fields.DateTime(required=True)
    modifyTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    releaseNote = fields.String(required=True)
    top = fields.String(required=True)
    source = fields.String(required=True)


class LocalReportSchema(Schema):
    """
    地方报道
    """
    title = fields.String(required=True)
    intro = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    sort = fields.Integer(required=True)
    top = fields.String(required=True)
    releaseNote = fields.String(required=True)


class PolicyReleaseDataSchema(_Schema):
    title = fields.String(required=True)
    number = fields.String(required=True)
    area = fields.String(required=True)
    policyTop = fields.String(required=True)
    profession = fields.String(required=True)
    policyTheme = fields.String(required=True)
    organization = fields.String(required=True)
    releaseFlag = fields.String(required=True)


class PolicyReleaseSchema(Schema):
    """
    政策发布
    """
    title = fields.String(required=True)
    number = fields.String(required=True)
    organization = fields.String(required=True)
    publisher = fields.String(required=True)
    releaseTime = fields.DateTime(required=True)
    modifyTime = fields.DateTime(required=True)
    policyTheme = fields.String(required=True)
    animalKeyword = fields.String(required=True)
    timerShaft = fields.String(required=True)
    policyBelong = fields.String(required=True)
    area = fields.String(required=True)
    businessPeople = fields.String(required=True)
    businessService = fields.String(required=True)
    profession = fields.String(required=True)
    policySort = fields.Integer(required=True)
    policyTop = fields.String(required=True)
    releaseFlag = fields.String(required=True)
    rows = fields.Nested('self', only=["title", "number", "organization", "publisher", "releaseTime", "modifyTime",
                                       "policyTheme", "animalKeyword", "timerShaft", "policyBelong",
                                       "area", "businessPeople", "businessService", "profession", "policySort",
                                       "policyTop", "releaseFlag"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(PolicyReleaseDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class EcosphereDataSchema(_Schema):
    ecosphereName = fields.String(required=True)


class EcosphereSchema(Schema):
    """
    生态圈维护
    """
    id = fields.Integer(required=True)
    ecosphereName = fields.String(required=True)
    rows = fields.Nested('self', only=["id", "ecosphereName"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(EcosphereDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class TimerShaftDataSchema(_Schema):
    timerShaftName = fields.String(required=True)


class TimerShaftSchema(Schema):
    """
    时间轴维护
    """
    id = fields.Integer(required=True)
    timerShaftName = fields.String(required=True)
    rows = fields.Nested('self', only=["id", "timerShaftName"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(TimerShaftDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class BusinessServiceDataSchema(_Schema):
    businessName = fields.String(required=True)


class BusinessServiceSchema(Schema):
    id = fields.Integer(required=True)
    businessName = fields.String(required=True)
    rows = fields.Nested('self', only=["id", "businessName"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(BusinessServiceDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class AreaServiceDataSchema(_Schema):
    areaName = fields.String(required=True)


class AreaServiceSchema(Schema):
    """
    区域数据维护
    """
    id = fields.Integer(required=True)
    areaName = fields.String(required=True)
    rows = fields.Nested('self', only=["id", "areaName"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(AreaServiceDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class SubjectClassificationDataSchema(_Schema):
    SubjectName = fields.String(required=True)


class SubjectClassificationSchema(_Schema):
    """
    主题分类维护
    @author:lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    SubjectName = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=["id", "SubjectName"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(SubjectClassificationDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class PolicyClassifyDataSchema(_Schema):
    policyName = fields.String(required=True)


class PolicyClassifySchema(_Schema):
    """
    政策分类维护
    @author:lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    policyName = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=["id", "policyName"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(PolicyClassifyDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class IndustrialParkDataSchema(_Schema):
    industrialName = fields.String(required=True)


class IndustrialParkSchema(_Schema):
    """
    产业园推荐
    @author:lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    industrialName = fields.String(validate=validate.Length(6, 12), required=True)
    href = fields.String(validate=validate.Length(6, 12), required=True)
    sort = fields.Integer(dump_only=True)
    top = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=["id", "industrialName", "href", "sort", "top"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(IndustrialParkDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class BaseManageDataSchema(_Schema):
    baseStyle = fields.String(required=True)
    baseBatc = fields.String(required=True)
    top = fields.String(required=True)
    baseName = fields.String(required=True)


class BaseManageSchema(_Schema):
    """
    示范基地管理
    @author:lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    baseName = fields.String(validate=validate.Length(6, 12), required=True)
    baseStyle = fields.String(validate=validate.Length(6, 12), required=True)
    baseBatc = fields.String(validate=validate.Length(6, 12), required=True)
    area = fields.String(validate=validate.Length(6, 12), required=True)
    policyUnit = fields.String(validate=validate.Length(6, 12), required=True)
    creator = fields.String(validate=validate.Length(6, 12), required=True)
    createTime = fields.Date(required=True)
    modifier = fields.String(validate=validate.Length(6, 12), required=True)
    modifyTime = fields.Date(required=True)
    sort = fields.Integer(dump_only=True)
    top = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self',
                         only=["id", "baseName", "baseStyle", "baseBatc", "area", "policyUnit", "creator", "createTime",
                               "modifier", "modifyTime", "sort", "top"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersNumberMap = fields.Nested(BaseManageDataSchema())
    parametersStringMap = fields.Nested(BaseManageDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class UserBrowsingMessageDataSchema(_Schema):
    bussinessType = fields.String(required=True)
    userType = fields.String(required=True)


class UserBrowsingMessageSchema(_Schema):
    """
    用户浏览信息
    @author:lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    userIp = fields.String(validate=validate.Length(6, 12), required=True)
    bussinessType = fields.String(validate=validate.Length(6, 12), required=True)
    userType = fields.String(validate=validate.Length(6, 12), required=True)
    systemEnvironment = fields.String(validate=validate.Length(6, 12), required=True)
    customerPremise = fields.String(validate=validate.Length(6, 12), required=True)
    userSystem = fields.String(validate=validate.Length(6, 12), required=True)
    userMachineCode = fields.String(validate=validate.Length(6, 12), required=True)
    userBrowsingTime = fields.Date(required=True)
    userInformationClassification = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self',
                         only=["id", "userIp", "bussinessType", "userType", "systemEnvironment", "customerPremise",
                               "userSystem", "userMachineCode", "userBrowsingTime", "userInformationClassification"],
                         many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(UserBrowsingMessageDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class UserSearchInfoDataSchema(_Schema):
    userSearchContent = fields.String(required=True)
    userType = fields.String(required=True)
    userSearchMethod = fields.String(required=True)


class UserSearchInfoSchema(_Schema):
    """
    用户搜索信息
    @author:lyfy
    :return:
    """
    userIp = fields.String(required=True)
    userLocation = fields.String(required=True)
    userSystem = fields.String(required=True)
    userMachineCode = fields.String(required=True)
    USearchContent = fields.String(required=True)
    USearchMethod = fields.String(required=True)
    USearchCondition = fields.String(required=True)
    SPClassify = fields.String(required=True)
    userType = fields.String(required=True)
    rows = fields.Nested('self', only=["userIp", "userLocation", "userSystem", "userMachineCode",
                                       "USearchContent", "USearchMethod", "USearchCondition",
                                       "SPClassify", "userType"], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(UserSearchInfoDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class PilotManagementDataSchema(_Schema):
    pilotName = fields.String(required=True)
    top = fields.String(required=True)


class PilotManagementSchema(_Schema):
    """
    试验区管理--查
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    pilotName = fields.String(validate=validate.Length(6, 12), required=True)
    creator = fields.String(validate=validate.Length(6, 12), required=True)
    createTime = fields.DateTime(dump_only=True)
    modifier = fields.String(validate=validate.Length(6, 12), required=True)
    modifyTime = fields.DateTime(dump_only=True)
    sort = fields.String(validate=validate.Length(6, 12), required=True)
    top = fields.String(validate=validate.Length(6, 12), required=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersNumberMap = fields.Nested(PilotManagementDataSchema())
    parametersStringMap = fields.Nested(PilotManagementDataSchema())
    rows = fields.Nested('self',
                         only=['id', 'pilotName', 'creator', 'createTime', 'modifier', 'modifyTime', 'sort', 'top'],
                         many=True)
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class SuggestionsDataSchema(_Schema):
    status = fields.String(required=True)


class SuggestionsSchema(_Schema):
    """
    建言献策
    @ author: lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(6, 12), required=True)
    unit = fields.String(validate=validate.Length(6, 12), required=True)
    pnumber = fields.String(validate=validate.Length(6, 12), required=True)
    email = fields.String(validate=validate.Length(6, 12), required=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    time = fields.DateTime(dump_only=True)
    status = fields.String(validate=validate.Length(6, 12), required=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(SuggestionsDataSchema())
    rows = fields.Nested('self', only=['id', 'name', 'unit', 'pnumber', 'email', 'title', 'time', 'status'],
                         many=True)
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class PolicyStatisticsDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)


class PolicyStatisticsSchema(_Schema):
    """
    政策统计列表
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    issuednumber = fields.String(validate=validate.Length(6, 12), required=True)
    company = fields.String(validate=validate.Length(6, 12), required=True)
    time = fields.DateTime(dump_only=True)
    policyaccess = fields.String(validate=validate.Length(6, 12), required=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(PolicyStatisticsDataSchema())
    rows = fields.Nested('self', only=['id', 'title', 'issuednumber', 'company', 'time', 'policyaccess'],
                         many=True)
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class JournalSystemDataSchema(_Schema):
    # data = fields.String(required=True)
    starttime = fields.String(required=True)
    operationtype = fields.String(required=True)
    operator = fields.String(required=True)
    endtime = fields.String(required=True)


class JournalSystemSchema(_Schema):
    """
    系统日志管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    modulename = fields.String(validate=validate.Length(6, 12), required=True)
    operationtype = fields.String(validate=validate.Length(6, 12), required=True)
    describe = fields.String(validate=validate.Length(6, 12), required=True)
    result = fields.String(validate=validate.Length(6, 12), required=True)
    operator = fields.String(validate=validate.Length(6, 12), required=True)
    ip = fields.String(validate=validate.Length(6, 12), required=True)
    operationdate = fields.DateTime(dump_only=True)
    creationtime = fields.DateTime(dump_only=True)
    rows = fields.Nested('self', only=['id', 'modulename', 'operationtype', 'describe', 'result', 'operator', 'ip',
                                       'operationdate', 'creationtime'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(JournalSystemDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class JournalPolicyDataSchema(_Schema):
    # data = fields.String(required=True)
    type = fields.String(required=True)
    starttime = fields.String(required=True)
    endtime = fields.String(required=True)


class JournalPolicySchema(_Schema):
    """
    政策日志管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    visiting = fields.String(validate=validate.Length(6, 12), required=True)
    visitorip = fields.String(validate=validate.Length(6, 12), required=True)
    country = fields.String(validate=validate.Length(6, 12), required=True)
    area = fields.String(validate=validate.Length(6, 12), required=True)
    province = fields.String(validate=validate.Length(6, 12), required=True)
    city = fields.String(validate=validate.Length(6, 12), required=True)
    district = fields.String(validate=validate.Length(6, 12), required=True)
    operator = fields.String(validate=validate.Length(6, 12), required=True)
    type = fields.String(validate=validate.Length(6, 12), required=True)
    describe = fields.String(validate=validate.Length(6, 12), required=True)
    time = fields.DateTime(dump_only=True)
    rows = fields.Nested('self', only=['id', 'visiting', 'visitorip', 'country', 'area', 'province', 'city',
                                       'district', 'operator', 'type', 'describe', 'time'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(JournalPolicyDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class AboutUsSchema(_Schema):
    """
    关于我们
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    firsttitle = fields.String(validate=validate.Length(6, 12), required=True)
    firstcontent = fields.String(validate=validate.Length(6, 12), required=True)
    secondtitle = fields.String(validate=validate.Length(6, 12), required=True)
    secondcontent = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=['id', 'firsttitle', 'firstcontent', 'secondtitle', 'secondcontent'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(JournalPolicyDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class MovePresentationDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)
    releaselogo = fields.String(required=True)


class MovePresentationSchema(_Schema):
    """
    移动端功能管理--报告管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    description = fields.String(validate=validate.Length(6, 12), required=True)
    company = fields.String(validate=validate.Length(6, 12), required=True)
    publisher = fields.String(validate=validate.Length(6, 12), required=True)
    publishtime = fields.DateTime(dump_only=True)
    creationtime = fields.DateTime(dump_only=True)
    modifier = fields.String(validate=validate.Length(6, 12), required=True)
    mtime = fields.DateTime(dump_only=True)
    sort = fields.String(validate=validate.Length(6, 12), required=True)
    releaselogo = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self',
                         only=['id', 'title', 'description', 'company', 'publisher', 'publishtime', 'creationtime',
                               'modifier', 'mtime', 'sort', 'releaselogo'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(MovePresentationDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class MoveServiceDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)


class MoveServiceSchema(_Schema):
    """
    移动端功能管理--服务管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    description = fields.String(validate=validate.Length(6, 12), required=True)
    founder = fields.String(validate=validate.Length(6, 12), required=True)
    creationtime = fields.DateTime(dump_only=True)
    modifier = fields.String(validate=validate.Length(6, 12), required=True)
    mtime = fields.DateTime(dump_only=True)
    sort = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self',
                         only=['id', 'title', 'description', 'founder', 'creationtime', 'modifier', 'mtime', 'sort'],
                         many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(MoveServiceDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class MoveHomePageSchema(_Schema):
    """
    移动端功能管理--活动首页管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    description = fields.String(validate=validate.Length(6, 12), required=True)
    founder = fields.String(validate=validate.Length(6, 12), required=True)
    creationtime = fields.DateTime(dump_only=True)
    modifier = fields.String(validate=validate.Length(6, 12), required=True)
    mtime = fields.DateTime(dump_only=True)
    sort = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self',
                         only=['id', 'title', 'description', 'founder', 'creationtime', 'modifier', 'mtime', 'sort'],
                         many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(MoveServiceDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class MoveVersionDataSchema(_Schema):
    # data = fields.String(required=True)
    nember = fields.String(required=True)


class MoveVersionSchema(_Schema):
    """
    移动端功能管理--版本管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    number = fields.String(validate=validate.Length(6, 12), required=True)
    information = fields.String(validate=validate.Length(6, 12), required=True)
    classification = fields.String(validate=validate.Length(6, 12), required=True)
    compulsoryrenewal = fields.String(validate=validate.Length(6, 12), required=True)
    founder = fields.String(validate=validate.Length(6, 12), required=True)
    creationtime = fields.DateTime(dump_only=True)
    modifier = fields.String(validate=validate.Length(6, 12), required=True)
    mtime = fields.DateTime(dump_only=True)
    rows = fields.Nested('self', only=['id', 'number', 'information', 'classification', 'compulsoryrenewal', 'founder',
                                       'creationtime', 'modifier', 'mtime'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(MoveVersionDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class MoveUserDataSchema(_Schema):
    # data = fields.String(required=True)
    phone = fields.String(required=True)


class MoveUserSchema(_Schema):
    """
    移动端功能管理-用户管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    phone = fields.Integer(dump_only=True)
    user = fields.String(validate=validate.Length(6, 12), required=True)
    model = fields.String(validate=validate.Length(6, 12), required=True)
    time = fields.DateTime(dump_only=True)
    logintime = fields.DateTime(dump_only=True)
    rows = fields.Nested('self', only=['id', 'phone', 'user', 'model', 'time', 'logintime'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(MoveUserDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class MoveBriefingDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)
    releaselogo = fields.String(required=True)


class MoveBriefingSchema(_Schema):
    """"
    移动端功能管理-简报管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    time = fields.DateTime(dump_only=True)
    releaselogo = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=['id', 'title', 'time', 'releaselogo'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(MoveBriefingDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class GuideToAffairsDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)


class GuideToAffairsSchema(_Schema):
    """"
    服务拓展--办事指南管理
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    description = fields.String(validate=validate.Length(6, 12), required=True)
    source = fields.String(validate=validate.Length(6, 12), required=True)
    publishtime = fields.DateTime(dump_only=True)
    creationtime = fields.DateTime(dump_only=True)
    founder = fields.String(validate=validate.Length(6, 12), required=True)
    renewing = fields.String(validate=validate.Length(6, 12), required=True)
    updatatime = fields.DateTime(dump_only=True)
    releaselogo = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=['id', 'title', 'description', 'source', 'publishtime', 'creationtime', 'founder',
                                       'renewing', 'updatatime', 'releaselogo'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(GuideToAffairsDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class GovernmentFundsDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)
    costcategory = fields.String(required=True)
    releaselogo = fields.String(required=True)


class GovernmentFundsSchema(_Schema):
    """
    服务拓展--政府性基金和行政事业型收费
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    costcategory = fields.String(validate=validate.Length(6, 12), required=True)
    publisher = fields.String(validate=validate.Length(6, 12), required=True)
    publishtime = fields.DateTime(dump_only=True)
    renewing = fields.String(validate=validate.Length(6, 12), required=True)
    updatatime = fields.DateTime(dump_only=True)
    releaselogo = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self',
                         only=['id', 'title', 'costcategory', 'publisher', 'publishtime', 'renewing', 'updatatime',
                               'releaselogo'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(GovernmentFundsDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class FavouredPolicyDataSchema(_Schema):
    # data = fields.String(required=True)
    title = fields.String(required=True)
    taxcategory = fields.String(required=True)
    releaselogo = fields.String(required=True)


class FavouredPolicySchema(_Schema):
    """
    服务拓展--双创税收优惠政策查询
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    title = fields.String(validate=validate.Length(6, 12), required=True)
    taxstage = fields.String(validate=validate.Length(6, 12), required=True)
    taxcategory = fields.String(validate=validate.Length(6, 12), required=True)
    publisher = fields.String(validate=validate.Length(6, 12), required=True)
    publishtime = fields.DateTime(dump_only=True)
    renewing = fields.String(validate=validate.Length(6, 12), required=True)
    updatatime = fields.DateTime(dump_only=True)
    releaselogo = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=['id', 'title', 'taxstage', 'taxcategory', 'publisher', 'publishtime', 'renewing',
                                       'updatatime', 'releaselogo'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(FavouredPolicyDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)


class CancellationAndDecentralizationDataSchema(_Schema):
    name = fields.String(required=True)
    releaselogo = fields.String(required=True)


class CancellationAndDecentralizationSchema(_Schema):
    """
    服务拓展--取消和下放的行政事项
    @ author：lyfy
    :return:
    """
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(6, 12), required=True)
    itemtype = fields.String(validate=validate.Length(6, 12), required=True)
    department = fields.String(validate=validate.Length(6, 12), required=True)
    publisher = fields.String(validate=validate.Length(6, 12), required=True)
    publishtime = fields.DateTime(dump_only=True)
    renewing = fields.String(validate=validate.Length(6, 12), required=True)
    updatatime = fields.DateTime(dump_only=True)
    releaselogo = fields.String(validate=validate.Length(6, 12), required=True)
    rows = fields.Nested('self', only=['id', 'name', 'itemtype', 'department', 'publisher', 'publishtime', 'renewing',
                                       'updatatime', 'releaselogo'], many=True)
    colmodel = fields.Nested('self', many=True)
    limit = fields.Integer(dump_only=True)
    parametersStringMap = fields.Nested(CancellationAndDecentralizationDataSchema())
    start = fields.Integer(dump_only=True)
    total = fields.Integer(dump_only=True)
    totalPageCount = fields.Integer(dump_only=True)
