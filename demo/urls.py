from django.urls import path, re_path
from demo import views

app_name = 'demo'

urlpatterns = [
    path('', views.index, name='index'),

    ##############DRF Demo START##############
    # path('rdf/', views.rdf, name='demo_rdf'),
    path('rdf/', views.CBV_View.as_view(), name='demo_rdf'),
    path('rdf/movie/', views.MovieView.as_view()),
    re_path('rdf/movie/(\d+)/', views.MovieView.as_view()),    
    
    ##############DRF END##############

    path('navbar/1/', views.navbar1, name='navbar1'),
    path('navbar/2/', views.navbar2, name='navbar2'),
    path('test/1/', views.test1, name='test1'),
    path('test/2/', views.test2, name='test2'),
    path('test/3/', views.test3, name='test3'),
    path('test/4/', views.test4, name='test4'),
]