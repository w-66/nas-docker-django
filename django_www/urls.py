from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # Bootstrap
    path('learn/bootstrap/01/', views.learn_bootstrap_01),
    path('learn/bootstrap/02/', views.learn_bootstrap_02),
    path('learn/bootstrap/03/', views.learn_bootstrap_03),
    path('learn/bootstrap/04/', views.learn_bootstrap_04),
    path('learn/bootstrap/05/', views.learn_bootstrap_05),
    # React learn
    path('learn/react/17/', views.learn_react_17),
    path('learn/react/16/', views.learn_react_16),
    path('learn/react/15/', views.learn_react_15),
    path('learn/react/14/', views.learn_react_14),
    path('learn/react/13/', views.learn_react_13),
    path('learn/react/12/', views.learn_react_12),
    path('learn/react/11/', views.learn_react_11),
    path('learn/react/10/', views.learn_react_10),
    path('learn/react/09/', views.learn_react_09),
    path('learn/react/08/', views.learn_react_08),
    path('learn/react/07/', views.learn_react_07),
    path('learn/react/06/', views.learn_react_06),
    path('learn/react/05/', views.learn_react_05),
    path('learn/react/04/', views.learn_react_04),
    path('learn/react/03/', views.learn_react_03),
    path('learn/react/02/', views.learn_react_02),
    path('learn/react/01/', views.learn_react_01),
    # JS learn
    path('learn/js/04/', views.learn_js_04),
    path('learn/js/03/', views.learn_js_03),
    path('learn/js/02/', views.learn_js_02),
    path('learn/js/01/', views.learn_js_01),
    # 页面图标
    #
    # 时间记录
    path('lifelog/', views.lifelog),
    path('lifelog/edit/<int:global_id>/', views.lifelog_edit),
    path('lifelog/log/', views.lifelog_log),
    path('lifelog/del/<int:global_id>/', views.lifelog_del),


    # 音乐列表
    path('music/list/', views.music_list),
    ##音乐列表编辑页
    path('music/list/edit/<int:global_id>/', views.music_list_edit),

    # 测试
    path('demo/test/', views.demo_test),
    path('demo/test01/', views.demo_test01),

    # index
    path('index/', views.index),
    # path('admin/', admin.site.urls),
]
