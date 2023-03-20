from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.base import View
# 该装饰器标记着一个视图被免除了中间件所确保的保护
from django.views.decorators.csrf import csrf_exempt
#
from rest_framework.views import APIView     # drf的api view
from rest_framework import serializers       # 序列化器
from rest_framework.response import Response # def的响应，更易读的格式
from rest_framework.generics import GenericAPIView
#
from demo.models import Movie


def index(request):
    return render(request, 'demo/index.html')



##############RDF Demo##############
##############FBV##############
# def rdf(request):
#     if request.method == "GET":
#         return HttpResponse('get')
#     return HttpResponse('post')
# CBV
class CBV_View(View):
    def get(self, request):
        return HttpResponse('get')
    def post(self, request):
        return HttpResponse('post')
# ##############导入DEF##############

# ##############简单的DRF demo##############
# class CBV_View(APIView):
#     def get(self, request):
#         print('GET date:', request.query_params)  # 获取get的数据
#         return HttpResponse('framework get')
#     def post(self, request):
#         print('date:', request.data)              # 获取post的数据
#         print('date2:', request._request)         # 通过原生Django 获取post的数据
#         return HttpResponse('framework post')
    
# ##############对一个表做五个接口，CRUD操作 START##############
# #------定义序列化器-------
# # class MovieSerializer(serializers.Serializer):
# #     name_ch = serializers.CharField(max_length=100, required=True)
# #     name_en = serializers.CharField(max_length=100)
# #     description = serializers.CharField(source="movie_synopsis", required=False)

# #     def create(self, validated_data):
# #         add_movie = Movie.objects.create(**self.validated_data)
# #         return add_movie
# #     def update(self, instance, validated_data):
# #         Movie.objects.filter(id=instance.pk).update(**validated_data)
# #         # update = Movie.objects.get(id=instance.pk)
# #         update = Movie.objects.get(id=instance.id)
# #         return update

# class MovieModelSerializer(serializers.ModelSerializer):
#     description = serializers.CharField(source='movie_synopsis')
#     class Meta:
#         model = Movie
#         # fields = ["name_ch","movie_synopsis"]  # 指定字段
#         # fields = "__all__"                       # 指定所有字段
#         exclude = ["movie_synopsis"]
    
# #===========查所有&添加数据#===========
# class MovieAPIView(APIView):
#     def get(self, request):
#         movies_list = Movie.objects.all()
#         serializer = MovieModelSerializer(instance=movies_list, many=True)
#         # return HttpResponse(serializer.data)
#         return Response(serializer.data)
    
#     def post(self, request):
#         # 数据校验
#         serializer = MovieModelSerializer(data=request.data)
#         if serializer.is_valid():
#             # print('data', request.data)
#             # Movie.objects.create(**serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# #===========查询一条,更新一条,删除一条
# class MovieDetailAPIView(APIView):
#     #===========查询一条
#     def get(self, request, id):
#         # movie_detail = Movie.objects.get(id=id)
#         movie_detail = Movie.objects.filter(id=id).first()
#         serializers = MovieModelSerializer(instance=movie_detail, many=False)
#         return Response(serializers.data)
#     #===========更新一条
#     def post(self, request, id):
#         update_data = Movie.objects.get(id=id)
#         serializer = MovieModelSerializer(instance=update_data, data=request.data)
#         if serializer.is_valid():
#             # print("更新数据ing", serializer.validated_data)  # >> 更新数据ing OrderedDict([('name_ch', '千与千寻'), ('name_en', 'Spirited Away'), ('movie_synopsis', '更新数据')])
#             # Movie.objects.filter(id=id).update(**serializer.validated_data)
#             # update = Movie.objects.filter(id=id).first()
#             # serializer.instance = update
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             print("更新数据失败")
#             return Response(serializer.errors)
#     #===========删除一条
#     def delete(self, request, id):
#         Movie.objects.get(pk=id).delete()
#         return Response()
# ##############对一个表做五个接口，CRUD操作 END##############
# ##############对一个表做五个接口，使用GenericAPIView##############
# from rest_framework.generics import GenericAPIView

#===========查所有&添加数据#===========
class MovieModelSerializer(serializers.ModelSerializer):
    # description = serializers.CharField(source='movie_synopsis')
    class Meta:
        model = Movie
        # fields = ["name_ch","movie_synopsis"]  # 指定字段
        fields = "__all__"                       # 指定所有字段
        # exclude = ["movie_synopsis"]
class MovieView(GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
        # v3
        # serializer = MovieModelSerializer(instance=self.get_queryset(), many=True)
        # return Response(serializer.data)
        # v2 
        # movies_list = self.get_queryset()
        # serializer = MovieModelSerializer(instance=self.movies_list, many=True)
        # v1
        # return HttpResponse(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # 数据校验
        if serializer.is_valid():
            # print('data', request.data)
            # Movie.objects.create(**serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#===========查询一条,更新一条,删除一条
class MovieDetailView(GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    lookup_field = 'id'
    #===========查询一条
    def get(self, request, id):
        serializers = self.get_serializer(instance=self.get_object(), many=False)
        # movie_detail = Movie.objects.get(id=id)
        # movie_detail = Movie.objects.filter(id=id).first()
        # serializers = MovieModelSerializer(instance=movie_detail, many=False)
        return Response(serializers.data)
    #===========更新一条
    def post(self, request, id):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)

        # update_data = Movie.objects.get(id=id)
        # serializer = MovieModelSerializer(instance=update_data, data=request.data)
        if serializer.is_valid():
            # print("更新数据ing", serializer.validated_data)  # >> 更新数据ing OrderedDict([('name_ch', '千与千寻'), ('name_en', 'Spirited Away'), ('movie_synopsis', '更新数据')])
            # Movie.objects.filter(id=id).update(**serializer.validated_data)
            # update = Movie.objects.filter(id=id).first()
            # serializer.instance = update
            serializer.save()
            return Response(serializer.data)
        else:
            print("更新数据失败")
            return Response(serializer.errors)
    #===========删除一条
    def delete(self, request, id):
        self.get_object().delete()
        # Movie.objects.get(pk=id).delete()
        return Response()
















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
    