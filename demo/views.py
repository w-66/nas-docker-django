from django.utils import timezone
from django.http import HttpResponseRedirect
from demo.models import Movie
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.base import View
# 该装饰器标记着一个视图被免除了中间件所确保的保护
from django.views.decorators.csrf import csrf_exempt
#


def index(request):
    return render(request, 'demo/index.html')



##############RDF Demo##############
##############FBV##############
# def rdf(request):
#     if request.method == "GET":
#         return HttpResponse('get')
#     return HttpResponse('post')
# CBV
# class CBV_View(View):
#     def get(self, request):
#         return HttpResponse('get')
#     def post(self, request):
#         return HttpResponse('post')
##############导入DEF##############
from rest_framework.views import APIView     # drf的api view
from rest_framework import serializers       # 序列化器
from rest_framework.response import Response # def的响应，更易读的格式
##############简单的DRF demo##############
class CBV_View(APIView):
    def get(self, request):
        print('GET date:', request.query_params)  # 获取get的数据
        return HttpResponse('framework get')
    def post(self, request):
        print('date:', request.data)              # 获取post的数据
        print('date2:', request._request)         # 通过原生Django 获取post的数据
        return HttpResponse('framework post')
##############对一个表做五个接口，CRUD操作##############
#------定义序列化器-------
class MovieSerializers(serializers.Serializer):
    name_ch = serializers.CharField(max_length=100, required=True)
    name_en = serializers.CharField(max_length=100)
    description = serializers.CharField(source="movie_synopsis", required=False)

    def create(self, validated_data):
        add_movie = Movie.objects.create(**self.validated_data)
        return add_movie
    def update(self, validated_data):
        update = Movie.objects.filter(id=id).update(**self.validated_data)
        return update
    
#===========查所有&添加数据#===========
class MovieAPIView(APIView):
    def get(self, request):
        movies_list = Movie.objects.all()
        serializer = MovieSerializers(instance=movies_list, many=True)
        # return HttpResponse(serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        # 数据校验
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            # print('data', request.data)
            # Movie.objects.create(**serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
#===========查询一条,更新一条
class MovieDetailAPIView(APIView):
    def get(self, request, id):
        # movie_detail = Movie.objects.get(id=id)
        movie_detail = Movie.objects.filter(id=id).first()
        serializers = MovieSerializers(instance=movie_detail, many=False)
        return Response(serializers.data)
    #===========更新一条
    def post(self, request, id):
        update_data = Movie.objects.get(id=id)
        serializer = MovieSerializers(instance=update_data, data=request.data)
        if serializer.is_valid():
            print("更新数据ing", serializer.validated_data)  # >> 更新数据ing OrderedDict([('name_ch', '千与千寻'), ('name_en', 'Spirited Away'), ('movie_synopsis', '更新数据')])
            Movie.objects.filter(id=id).update(**serializer.validated_data)
            update = Movie.objects.filter(id=id).first()
            serializer.instance = update
            # serializer.save()
            return Response(serializer.data)
        else:
            print("更新数据失败")
            return Response(serializer.errors)

##############其他Demo##############
def navbar1(request):
    return render(request, 'demo/navbar1.html',)

def navbar2(request):
    return render(request, 'demo/navbar2.html',)

def test1(request):

    return render(request, 'demo/test1.html')
    
def test2(request):

    return render(request, 'demo/test2.html')
    
def test3(request):
    return render(request, 'demo/test3.html')
    
def test4(request):
    return render(request, 'demo/test4.html')
    