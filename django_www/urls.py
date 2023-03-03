from django.contrib import admin

from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from app01.views import index, learn_bootstrap, learn_js, learn_react, lifelog, music
from app01.views import login, task, lifelog_v2, chart


urlpatterns = [
    # Django 自带 admin管理页面
    path('admin/', admin.site.urls),

    path("app02/", include('app02.urls')),
    path('polls/', include('polls.urls')),
    path('demo/', include('demo.urls')),
    # Demo
    # path("demo/uploadfile/", demo.demo_uploadfile),
    # path("demo/1/", demo.demo_1),
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}, name='media'),

    # Bootstrap
    path('learn/bootstrap/01/', learn_bootstrap.learn_bootstrap_01),
    path('learn/bootstrap/02/', learn_bootstrap.learn_bootstrap_02),
    path('learn/bootstrap/03/', learn_bootstrap.learn_bootstrap_03),
    path('learn/bootstrap/04/', learn_bootstrap.learn_bootstrap_04),
    path('learn/bootstrap/05/', learn_bootstrap.learn_bootstrap_05),
    path('learn/bootstrap/06/', learn_bootstrap.learn_bootstrap_06),
    # React learn
    path('learn/react/17/', learn_react.learn_react_17),
    path('learn/react/16/', learn_react.learn_react_16),
    path('learn/react/15/', learn_react.learn_react_15),
    path('learn/react/14/', learn_react.learn_react_14),
    path('learn/react/13/', learn_react.learn_react_13),
    path('learn/react/12/', learn_react.learn_react_12),
    path('learn/react/11/', learn_react.learn_react_11),
    path('learn/react/10/', learn_react.learn_react_10),
    path('learn/react/09/', learn_react.learn_react_09),
    path('learn/react/08/', learn_react.learn_react_08),
    path('learn/react/07/', learn_react.learn_react_07),
    path('learn/react/06/', learn_react.learn_react_06),
    path('learn/react/05/', learn_react.learn_react_05),
    path('learn/react/04/', learn_react.learn_react_04),
    path('learn/react/03/', learn_react.learn_react_03),
    path('learn/react/02/', learn_react.learn_react_02),
    path('learn/react/01/', learn_react.learn_react_01),
    # JS learn
    path('learn/js/04/', learn_js.learn_js_04),
    path('learn/js/03/', learn_js.learn_js_03),
    path('learn/js/02/', learn_js.learn_js_02),
    path('learn/js/01/', learn_js.learn_js_01),


    # 图表
    path('chart/list/', chart.chart_list),
    path('chart/bar/ajax/', chart.chart_bar_ajax),
    
    # 登录
    path('login/', login.login),
    path('logout/', login.logout),
    path('auth/code/', login.auth_code),

    # 任务管理
    path('task/', task.task_ajax),
    path('task/add/', task.task_ajax_add),
    path('task/edit/<int:id>/', task.task_edit),
    path('task/del/<int:id>/', task.task_del),

    # 自建 Admin
    # path('admin/', admin.admin),
    # path('admin/add/', admin.admin_add),
    # path('admin/edit/<int:id>/', admin.admin_edit),
    # path('admin/del/<int:id>/', admin.admin_del),

    # 时间记录
    path('lifelog/', lifelog.lifelog),
    path('lifelog/edit/<int:id>/', lifelog.lifelog_edit),
    path('lifelog/log/', lifelog.lifelog_log),
    path('lifelog/del/<int:global_id>/', lifelog.lifelog_del),
    
    # 时间记录 v2
    path('lifelog/v2/', lifelog_v2.lifelog_v2),
    path("lifelog/v2/add/ajax/", lifelog_v2.lifelog_v2_add_ajax),
    path('lifelog/v2/del/<int:global_id>/', lifelog_v2.lifelog_v2_del),
    

    # 音乐列表
    path('music/list/', music.music_list),
    ##音乐列表编辑页
    path('music/list/edit/<int:global_id>/', music.music_list_edit),

    # index
    path('index/', index.index),
]
