from django.urls import path, re_path
from demo import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),

    ##############DRF Demo START##############
    # path('drf/', views.rdf, name='demo_rdf'),
    # path('drf/', views.CBV_View.as_view(), name='demo_rdf'),
    # ----
    # path('drf/movie/', views.MovieView.as_view()),
    # re_path('drf/movie/(?P<pk>\d+)/', views.MovieDetailView.as_view()),    # 与下相同
    # path('drf/movie/<int:id>/', views.MovieDetailView.as_view()),    
    # ----使用ViewSet，两条路由使用同一个类
    # path("drf/movie/", views.PublishView.as_view({'get':'get_all', 'post':'add_item'})),
    # path("drf/movie/<int:id>/", views.PublishView.as_view({'get':'get_item', 'put':'update_item', 'delete':'delete_item'})),
    # 
    path("drf/movie/", views.MovieModelViewSet.as_view({'get':'list', 'post':'create'})),
    path("drf/movie/<int:id>/", views.MovieModelViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'})),

    ##############DRF END##############
    

    path('navbar/1/', views.navbar1, name='navbar1'),
    path('navbar/2/', views.navbar2, name='navbar2'),
    path('test/1/', views.test1, name='test1'),
    path('test/2/', views.test2, name='test2'),
    path('test/3/', views.test3, name='test3'),
    path('test/4/', views.test4, name='test4'),
]