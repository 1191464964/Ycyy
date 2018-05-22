# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from flask import Blueprint

from .icnpp import (MediaView, ActivityManageView, MascotView, GuestView, HallView, CenterNewView,
                    ActivityTypeView, LocalNewView, DepartmentView, policyView, LocalReportView,
                    IndexView, PolicyStatisticsView, JournalSystemView, JournalPolicyView,
                    AboutUsView, MovePresentationAddView, MovePresentationDeleteView, MovePresentationUpdateView,
                    MovePresentationView, MoveServiceAddView, MoveServiceDeleteView, MoveServiceUpdateView,
                    MoveServiceView, MoveHomePageAddView, MoveHomePageDeleteView, MoveHomePageUpdateView,
                    MoveHomePageView, MoveVersionAddView, MoveVersionDeleteView, MoveVersionUpdateView,
                    MoveVersionView, MoveUserDeleteView, MoveUserView, MoveBriefingAddView,
                    MoveBriefingDeleteView, MoveBriefingUpdateView, MoveBriefingView, GuideToAffairsAddView,
                    GuideToAffairsDeleteView, GuideToAffairsUpdateView, GuideToAffairsView,
                    GovernmentFundsAddView, GovernmentFundsDeleteView, GovernmentFundsUpdateView, GovernmentFundsView,
                    FavouredPolicyAddView, FavouredPolicyDeleteView, FavouredPolicyUpdateView, FavouredPolicyView,
                    CancellationAndDecentralizationAddView, CancellationAndDecentralizationDeleteView,
                    CancellationAndDecentralizationUpdateView, CancellationAndDecentralizationView, SuggestionsView,
                    SuggestionsDeleteView, PilotManagementAddView, PilotManagementDeleteView, PilotManagementUpdateView,
                    PilotManagementView, UserSearchInfoView, UserBrowsingMessageView, BaseManageAddView,
                    BaseManageDeleteView, BaseManageUpdateView, BaseManageView, IndustrialParkAddView,
                    IndustrialParkDeleteView, IndustrialParkUpdateView, IndustrialParkView, PolicyClassifyAddView,
                    PolicyClassifyDeleteView, PolicyClassifyUpdateView, PolicyClassifyView,
                    SubjectClassificationAddView,
                    SubjectClassificationDeleteView, SubjectClassificationUpdateView, SubjectClassificationView,
                    AreaServiceAddView, AreaServiceDeleteView, AreaServiceUpdateView, AreaServiceView,
                    BusinessServiceAddView, BusinessServiceDeleteView, BusinessServiceUpdateView, BusinessServiceView,
                    TimerShaftView, EcosphereUpdateView, EcosphereView, PolicyReleaseAddView, PolicyReleaseDeleteView,
                    PolicyReleaseUpdateView, PolicyReleaseView)

icnpp = Blueprint('icnpp', __name__)

icnpp.add_url_rule(
    '/',
    view_func=IndexView.as_view('/'),
    endpoint="innp_only_andminindex",
    methods=["POST", "GET"]
)

icnpp.add_url_rule(
    '/mediaview',
    view_func=MediaView.as_view("mediaview"),
    endpoint="AddMedia",
    methods=["POST"]
)

icnpp.add_url_rule(
    '/addmanage',
    view_func=ActivityManageView.as_view("addmanage"),
    endpoint="addmanage",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/mascot",
    view_func=MascotView.as_view("mascot"),
    endpoint="addmascot",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/guest",
    view_func=GuestView.as_view("guest"),
    endpoint="addguest",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/hall",
    view_func=HallView.as_view("hall"),
    endpoint="addhall",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/atype",
    view_func=ActivityTypeView.as_view("atype"),
    endpoint="addactivitytype",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/cnew",
    view_func=CenterNewView.as_view("cnew"),
    endpoint="addcenternew",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/lnew",
    view_func=LocalNewView.as_view("lnew"),
    endpoint="addlocalnew",
    methods=["POST"]
)
icnpp.add_url_rule(
    "/dp",
    view_func=DepartmentView.as_view("dp"),
    endpoint="adddepartment",
    methods=["POST"]
)

icnpp.add_url_rule(
    "/policy",
    view_func=policyView.as_view("policy"),
    endpoint="Addpolicy",
    methods=["POST"]
)

icnpp.add_url_rule(
    "lpview",
    view_func=LocalReportView.as_view("lpview"),
    endpoint="AddLocalReport",
    methods=["POST"]
)
# ---------
icnpp.add_url_rule(
    # 政策发布--增
    # 需传入所有字段
    '/policyreleaseadd',
    view_func=PolicyReleaseAddView.as_view('policyreleaseadd'),
    endpoint="innp_only_policyreleaseadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策发布--删
    # 需传入id
    '/policyreleasedelete',
    view_func=PolicyReleaseDeleteView.as_view('policyreleasedelete'),
    endpoint="innp_only_policyreleasedelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策发布--改
    # 需传入pageNum，pageSize，id
    '/policyreleaseupdate',
    view_func=PolicyReleaseUpdateView.as_view('policyreleaseupdate'),
    endpoint="innp_only_policyreleaseupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策发布--查
    # 需传入pageNum，pageSize，title,number,area,policyTop,profession,policyTheme,organization,releaseFlag
    '/policyrelease',
    view_func=PolicyReleaseView.as_view('policyrelease'),
    endpoint="innp_only_policyrelease",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 生态圈维护--改
    # 需传入pageNum，pageSize，id
    '/ecosphereupdate',
    view_func=EcosphereUpdateView.as_view('ecosphereupdate'),
    endpoint="innp_only_ecosphereupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 生态圈维护--查
    # 需传入pageNum，pageSize，ecosphereName
    '/ecosphere',
    view_func=EcosphereView.as_view('ecosphere'),
    endpoint="innp_only_ecosphere",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 时间轴维护--查
    # 需传入pageNum，pageSize，timerShaftName
    '/timershaft',
    view_func=TimerShaftView.as_view('timershaft'),
    endpoint="innp_only_timershaft",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 行业数据维护--增
    # 需传入所有字段
    '/businessserviceadd',
    view_func=BusinessServiceAddView.as_view('businessserviceadd'),
    endpoint="innp_only_businessserviceadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 行业数据维护--删
    # 需传入id
    '/businessservicedelete',
    view_func=BusinessServiceDeleteView.as_view('businessservicedelete'),
    endpoint="innp_only_businessservicedelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 行业数据维护--改
    # 需传入pageNum，pageSize，id
    '/businessserviceupdate',
    view_func=BusinessServiceUpdateView.as_view('businessserviceupdate'),
    endpoint="innp_only_businessserviceupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 行业数据维护--查
    # 需传入pageNum，pageSize，businessName
    '/businessservice',
    view_func=BusinessServiceView.as_view('businessservice'),
    endpoint="innp_only_businessservice",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 区域数据维护--增
    # 需传入所有字段
    '/areaserviceadd',
    view_func=AreaServiceAddView.as_view('areaserviceadd'),
    endpoint="innp_only_areaserviceadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 区域数据维护--删
    # 需传入id
    '/areaservicedelete',
    view_func=AreaServiceDeleteView.as_view('areaservicedelete'),
    endpoint="innp_only_areaservicedelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 区域数据维护--改
    # 需传入pageNum，pageSize，id
    '/areaserviceupdate',
    view_func=AreaServiceUpdateView.as_view('areaserviceupdate'),
    endpoint="innp_only_areaserviceupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 区域数据维护--查
    # 需传入pageNum，pageSize，areaName
    '/areaservice',
    view_func=AreaServiceView.as_view('areaservice'),
    endpoint="innp_only_areaservice",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 主题分类维护--增
    # 需传入所有字段
    '/subjectclassificationadd',
    view_func=SubjectClassificationAddView.as_view('subjectclassificationadd'),
    endpoint="innp_only_subjectclassificationadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 主题分类维护--删
    # 需传入id
    '/subjectclassificationdelete',
    view_func=SubjectClassificationDeleteView.as_view('subjectclassificationdelete'),
    endpoint="innp_only_subjectclassificationdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 主题分类维护--改
    # 需传入pageNum，pageSize，id
    '/subjectclassificationupdate',
    view_func=SubjectClassificationUpdateView.as_view('subjectclassificationupdate'),
    endpoint="innp_only_subjectclassificationupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 主题分类维护--查
    # 需传入pageNum，pageSize，SubjectName
    '/subjectclassification',
    view_func=SubjectClassificationView.as_view('subjectclassification'),
    endpoint="innp_only_subjectclassification",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策分类维护--增
    # 需传入所有字段
    '/policyclassifyadd',
    view_func=PolicyClassifyAddView.as_view('policyclassifyadd'),
    endpoint="innp_only_policyclassifyadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策分类维护--删
    # 需传入id
    '/policyclassifydelete',
    view_func=PolicyClassifyDeleteView.as_view('policyclassifydelete'),
    endpoint="innp_only_policyclassifydelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策分类维护--改
    # 需传入pageNum，pageSize，id
    '/policyclassifyupdate',
    view_func=PolicyClassifyUpdateView.as_view('policyclassifyupdate'),
    endpoint="innp_only_policyclassifyupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策分类维护--查
    # 需传入pageNum，pageSize，policyName
    '/policyclassify',
    view_func=PolicyClassifyView.as_view('policyclassify'),
    endpoint="innp_only_policyclassify",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 产业园推荐--增
    # 需传入所有字段
    '/industrialparkadd',
    view_func=IndustrialParkAddView.as_view('industrialparkadd'),
    endpoint="innp_only_industrialparkadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 产业园推荐--删
    # 需传入id
    '/industrialparkdelete',
    view_func=IndustrialParkDeleteView.as_view('industrialparkdelete'),
    endpoint="innp_only_industrialparkdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 产业园推荐--改
    # 需传入pageNum，pageSize，id
    '/industrialparkupdate',
    view_func=IndustrialParkUpdateView.as_view('industrialparkupdate'),
    endpoint="innp_only_industrialparkupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 产业园推荐--查
    # 需传入pageNum，pageSize，industrialName
    '/industrialpark',
    view_func=IndustrialParkView.as_view('industrialpark'),
    endpoint="innp_only_industrialpark",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 示范基地管理--增
    # 需传入所有字段
    '/basemanageadd',
    view_func=BaseManageAddView.as_view('basemanageadd'),
    endpoint="innp_only_basemanageadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 示范基地管理--删
    # 需传入id
    '/basemanagedelete',
    view_func=BaseManageDeleteView.as_view('basemanagedelete'),
    endpoint="innp_only_basemanagedelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 示范基地管理--改
    # 需传入pageNum，pageSize，id
    '/basemanageupdate',
    view_func=BaseManageUpdateView.as_view('basemanageupdate'),
    endpoint="innp_only_basemanageupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 示范基地管理--查
    # 需传入pageNum，pageSize，baseStyle,baseBatc,baseName,top
    '/basemanage',
    view_func=BaseManageView.as_view('basemanage'),
    endpoint="innp_only_basemanage",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 用户浏览信息--查
    # 需传入pageNum，pageSize，bussinessType,userType
    '/userbrowsingmessage',
    view_func=UserBrowsingMessageView.as_view('userbrowsingmessage'),
    endpoint="innp_only_userbrowsingmessage",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 用户搜索信息--查
    # 需传入pageNum，pageSize，userType,userSearchContent,userSearchMethod
    '/usersearchinfo',
    view_func=UserSearchInfoView.as_view('usersearchinfo'),
    endpoint="innp_only_usersearchinfo",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 试验区管理--增
    # 需传入所有字段
    '/pilotmanagementadd',
    view_func=PilotManagementAddView.as_view('pilotmanagementadd'),
    endpoint="innp_only_pilotmanagementadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 试验区管理--删
    # 需传入id
    '/pilotmanagementdelete',
    view_func=PilotManagementDeleteView.as_view('pilotmanagementdelete'),
    endpoint="innp_only_pilotmanagementdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 试验区管理--改
    # 需传入pageNum，pageSize，id
    '/pilotmanagementupdate',
    view_func=PilotManagementUpdateView.as_view('pilotmanagementupdate'),
    endpoint="innp_only_pilotmanagementupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 试验区管理--查
    # 需传入pageNum，pageSize，pilotName,top
    '/pilotmanagement',
    view_func=PilotManagementView.as_view('pilotmanagement'),
    endpoint="innp_only_pilotmanagement",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 建言献策--删
    # 需传入id
    '/suggestionsdelete',
    view_func=SuggestionsDeleteView.as_view('suggestionsdelete'),
    endpoint="innp_only_suggestionsdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 建言献策--查
    # 需传入pageNum，pageSize，status
    '/suggestions',
    view_func=SuggestionsView.as_view('suggestions'),
    endpoint="innp_only_suggestions",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 政策统计
    # 需传入pageNum，pageSize，title
    '/policystatistics',
    view_func=PolicyStatisticsView.as_view('policystatistics'),
    endpoint="innp_only_policystatistics",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 日志管理--系统日志管理
    # 需传入pageNum，pageSize，modulename，operator，starttime，endtime
    '/journalsystem',
    view_func=JournalSystemView.as_view('journalsystem'),
    endpoint="innp_only_journalsystem",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 日志管理--政策日志管理
    # 需传入pageNum，pageSize，type，starttime，endtime
    '/journalpolicy',
    view_func=JournalPolicyView.as_view('journalpolicy'),
    endpoint="innp_only_journalpolicy",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 关于我们
    # 需传入pageNum，pageSize
    '/aboutus',
    view_func=AboutUsView.as_view('aboutus'),
    endpoint="innp_only_aboutus",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--报告管理--增
    # 需传入表中各字段
    '/movepresentationadd',
    view_func=MovePresentationAddView.as_view('movepresentationadd'),
    endpoint="innp_only_movepresentationadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--报告管理--删
    # 需传入id
    '/movepresentationdelete',
    view_func=MovePresentationDeleteView.as_view('movepresentationdelete'),
    endpoint="innp_only_movepresentationdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--报告管理--改
    # 需传入表中各字段
    '/movepresentationupdate',
    view_func=MovePresentationUpdateView.as_view('movepresentationupdate'),
    endpoint="innp_only_movepresentationupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--报告管理--查
    # 需传入pageNum，pageSize，title，releaselogo
    '/movepresentation',
    view_func=MovePresentationView.as_view('movepresentation'),
    endpoint="innp_only_movepresentation",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--服务管理--增
    # 需传入表中各字段
    '/moveserviceadd',
    view_func=MoveServiceAddView.as_view('moveserviceadd'),
    endpoint="innp_only_moveserviceadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--服务管理--删
    # 需传入id
    '/moveservicedelete',
    view_func=MoveServiceDeleteView.as_view('moveservicedelete'),
    endpoint="innp_only_moveservicedelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--服务管理--改
    # 需传入表中各字段
    '/moveserviceupdate',
    view_func=MoveServiceUpdateView.as_view('moveserviceupdate'),
    endpoint="innp_only_moveserviceupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--服务管理--查
    # 需传入pageNum，pageSize，title
    '/moveservice',
    view_func=MoveServiceView.as_view('moveservice'),
    endpoint="innp_only_moveservice",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--活动首页管理--增
    # 需传入表中各字段
    '/movehomepageadd',
    view_func=MoveHomePageAddView.as_view('movehomepageadd'),
    endpoint="innp_only_movehomepageadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--活动首页管理--删
    # 需传入id
    '/movehomepagedelete',
    view_func=MoveHomePageDeleteView.as_view('movehomepagedelete'),
    endpoint="innp_only_movehomepagedelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--活动首页管理--改
    # 需传入表中各字段
    '/movehomepageupdate',
    view_func=MoveHomePageUpdateView.as_view('movehomepageupdate'),
    endpoint="innp_only_movehomepageupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--活动首页管理--查
    # 需传入pageNum，pageSize，title
    '/movehomepage',
    view_func=MoveHomePageView.as_view('movehomepage'),
    endpoint="innp_only_movehomepage",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--版本管理--增
    # 需传入表中各字段
    '/moveversionadd',
    view_func=MoveVersionAddView.as_view('moveversionadd'),
    endpoint="innp_only_moveversionadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--版本管理--删
    # 需传入id
    '/moveversiondelete',
    view_func=MoveVersionDeleteView.as_view('moveversiondelete'),
    endpoint="innp_only_moveversiondelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--版本管理--改
    # 需传入表中各字段
    '/moveversionupdate',
    view_func=MoveVersionUpdateView.as_view('moveversionupdate'),
    endpoint="innp_only_moveversionupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--版本管理--查
    # 需传入pageNum，pageSize，title
    '/moveversion',
    view_func=MoveVersionView.as_view('moveversion'),
    endpoint="innp_only_moveversion",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--用户管理--删
    # 需传入id
    '/moveuserdelete',
    view_func=MoveUserDeleteView.as_view('moveuserdelete'),
    endpoint="innp_only_moveuserdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--用户管理--查
    # 需传入pageNum，pageSize，title
    '/moveuser',
    view_func=MoveUserView.as_view('moveuser'),
    endpoint="innp_only_moveuser",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--简报管理--增
    # 需传入表中各字段
    '/movebriefingadd',
    view_func=MoveBriefingAddView.as_view('movebriefingadd'),
    endpoint="innp_only_movebriefingadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--简报管理--删
    # 需传入id
    '/movebriefingdelete',
    view_func=MoveBriefingDeleteView.as_view('movebriefingdelete'),
    endpoint="innp_only_movebriefingdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--简报管理--改
    # 需传入表中各字段
    '/movebriefingupdate',
    view_func=MoveBriefingUpdateView.as_view('movebriefingupdate'),
    endpoint="innp_only_movebriefingupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 移动端功能管理--简报管理--查
    # 需传入pageNum，pageSize，title
    '/movebriefing',
    view_func=MoveBriefingView.as_view('movebriefing'),
    endpoint="innp_only_movebriefing",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--办事指南--增
    # 需传入表中各字段
    '/guidetoaffairsadd',
    view_func=GuideToAffairsAddView.as_view('guidetoaffairsadd'),
    endpoint="innp_only_guidetoaffairsadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--办事指南--删
    # 需传入id
    '/guidetoaffairsdelete',
    view_func=GuideToAffairsDeleteView.as_view('guidetoaffairsdelete'),
    endpoint="innp_only_guidetoaffairsdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--办事指南--改
    # 需传入表中各字段
    '/guidetoaffairsupdate',
    view_func=GuideToAffairsUpdateView.as_view('guidetoaffairsupdate'),
    endpoint="innp_only_guidetoaffairsupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--办事指南--查
    # 需传入pageNum，pageSize，title
    '/guidetoaffairs',
    view_func=GuideToAffairsView.as_view('guidetoaffairs'),
    endpoint="innp_only_guidetoaffairs",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--政府性基金和行政事业型收费--增
    # 需传入表中各字段
    '/governmentfundsadd',
    view_func=GovernmentFundsAddView.as_view('governmentfundsadd'),
    endpoint="innp_only_governmentfundsadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--政府性基金和行政事业型收费--删
    # 需传入id
    '/governmentfundsdelete',
    view_func=GovernmentFundsDeleteView.as_view('governmentfundsdelete'),
    endpoint="innp_only_governmentfundsdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--政府性基金和行政事业型收费--改
    # 需传入表中各字段
    '/governmentfundsupdate',
    view_func=GovernmentFundsUpdateView.as_view('governmentfundsupdate'),
    endpoint="innp_only_governmentfundsupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--政府性基金和行政事业型收费--查
    # 需传入pageNum，pageSize，title
    '/governmentfunds',
    view_func=GovernmentFundsView.as_view('governmentfunds'),
    endpoint="innp_only_governmentfunds",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--双创税收优惠政策查询--增
    # 需传入表中各字段
    '/favouredpolicyadd',
    view_func=FavouredPolicyAddView.as_view('favouredpolicyadd'),
    endpoint="innp_only_favouredpolicyadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--双创税收优惠政策查询--删
    # 需传入id
    '/favouredpolicydelete',
    view_func=FavouredPolicyDeleteView.as_view('favouredpolicydelete'),
    endpoint="innp_only_favouredpolicydelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--双创税收优惠政策查询--改
    # 需传入表中各字段
    '/favouredpolicyupdate',
    view_func=FavouredPolicyUpdateView.as_view('favouredpolicyupdate'),
    endpoint="innp_only_favouredpolicyupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--双创税收优惠政策查询--查
    # 需传入pageNum，pageSize，title
    '/favouredpolicy',
    view_func=FavouredPolicyView.as_view('favouredpolicy'),
    endpoint="innp_only_favouredpolicy",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--取消和下放的行政事项--增
    # 需传入表中各字段
    '/cancellationanddecentralizationadd',
    view_func=CancellationAndDecentralizationAddView.as_view('cancellationanddecentralizationadd'),
    endpoint="innp_only_cancellationanddecentralizationadd",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--取消和下放的行政事项--删
    # 需传入id
    '/cancellationanddecentralizationdelete',
    view_func=CancellationAndDecentralizationDeleteView.as_view('cancellationanddecentralizationdelete'),
    endpoint="innp_only_cancellationanddecentralizationdelete",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--取消和下放的行政事项--改
    # 需传入表中各字段
    '/cancellationanddecentralizationupdate',
    view_func=CancellationAndDecentralizationUpdateView.as_view('cancellationanddecentralizationupdate'),
    endpoint="innp_only_cancellationanddecentralizationupdate",
    methods=["POST"]
)

icnpp.add_url_rule(
    # 服务拓展--取消和下放的行政事项--查
    # 需传入pageNum，pageSize，title
    '/cancellationanddecentralization',
    view_func=CancellationAndDecentralizationView.as_view('cancellationanddecentralization'),
    endpoint="innp_only_cancellationanddecentralization",
    methods=["POST"]
)
