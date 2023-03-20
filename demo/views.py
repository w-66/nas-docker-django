from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse
from django.views import generic
from django.views.generic.base import View
# 该装饰器标记着一个视图被免除了中间件所确保的保护
# from django.views.decorators.csrf import csrf_exempt
#
from rest_framework import serializers       # 序列化器
from rest_framework.response import Response # def的响应，更易读的格式
# from rest_framework.views import APIView     # drf的api view
# from rest_framework.generics import GenericAPIView

#
from demo.models import Movie


def index(request):
    return render(request, 'demo/index.html')



##############RDF Demo##############
#
from rest_framework.viewsets import ModelViewSet
class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"       # 指定所有字段

class MovieModelViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    lookup_field = 'id'     # 使用 id 作为传参名称(默认是pk)


##############将五个接口放到一个视图的实现（具体业务还差一步）将五个接口放到一个视图的实现（具体业务还差一步）
# from rest_framework.viewsets import ViewSet
# class MovieModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = "__all__"       # 指定所有字段
# class PublishView(ViewSet):
#     def get_all(self, request):            # 查询所有
#         return Response('get_all')         
#     def add_item(self, request):           # 添加一条记录
#         return Response('add_item')
#     def get_item(self, request, id):       # 查询一条记录
#         return Response('get_item')        
#     def update_item(self, request, id):    # 更新一条记录
#         return Response('update_item')
#     def delete_item(self, request, id):    # 删除一条记录
#         return Response('delete_item')     

# # ##############再次封装mixins 混合类 v4##############
# # from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# # class MovieModelSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Movie
# #         fields = "__all__"       # 指定所有字段

# # class MovieView(ListCreateAPIView):            # 查询所有; 添加一条记录
# #     queryset = Movie.objects.all()
# #     serializer_class = MovieModelSerializer

# # class MovieDetailView(RetrieveUpdateDestroyAPIView):  # 查询一条记录，更新一条记录, 删除一条记录
# #     queryset = Movie.objects.all()
# #     serializer_class = MovieModelSerializer
# #     lookup_field = 'id'                               # 使用 id 作为默认传参名称


# ##############再次封装 v3##############
# # # 将下面注释的代码的封装(def自带封装的方法工具)
# # from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

# # class MovieModelSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Movie
# #         fields = "__all__"       # 指定所有字段

# # class MovieView(GenericAPIView, ListModelMixin, CreateModelMixin):
# #     queryset = Movie.objects.all()
# #     serializer_class = MovieModelSerializer

# #     def get(self, request):
# #         return self.list(request)                # 查询所有数据
# #     def post(self, request):
# #         return self.create(request=request)      # 添加一条数据

# # class MovieDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
# #     queryset = Movie.objects.all()
# #     serializer_class = MovieModelSerializer
# #     lookup_field = 'id'                          # 修改查询形参的名称(默认为pk)
# #     def get(self, request, id):
# #         return self.retrieve(request,id)         # 查询一条记录
# #     def put(self, request, id):
# #         return self.update(request, id)          # 更新一条记录
# #     def delete(self, request, id):
# #         return self.destroy(request, id)         # 删除一条记录

# # # ##############FBV##############
# # # # def rdf(request):
# # # #     if request.method == "GET":
# # # #         return HttpResponse('get')
# # # #     return HttpResponse('post')

# # # # ##############简单的DRF demo##############
# # # # class CBV_View(APIView):
# # # #     def get(self, request):
# # # #         print('GET date:', request.query_params)  # 获取get的数据
# # # #         return HttpResponse('framework get')
# # # #     def post(self, request):
# # # #         print('date:', request.data)              # 获取post的数据
# # # #         print('date2:', request._request)         # 通过原生Django 获取post的数据
# # # #         return HttpResponse('framework post')
    
# # # # ##############对一个表做五个接口，CRUD操作 START##############
# # # # #------定义序列化器-------
# # # # # class MovieSerializer(serializers.Serializer):
# # # # #     name_ch = serializers.CharField(max_length=100, required=True)
# # # # #     name_en = serializers.CharField(max_length=100)
# # # # #     description = serializers.CharField(source="movie_synopsis", required=False)

# # # # #     def create(self, validated_data):
# # # # #         add_movie = Movie.objects.create(**self.validated_data)
# # # # #         return add_movie
# # # # #     def update(self, instance, validated_data):
# # # # #         Movie.objects.filter(id=instance.pk).update(**validated_data)
# # # # #         # update = Movie.objects.get(id=instance.pk)
# # # # #         update = Movie.objects.get(id=instance.id)
# # # # #         return update

# # # # class MovieModelSerializer(serializers.ModelSerializer):
# # # #     description = serializers.CharField(source='movie_synopsis')
# # # #     class Meta:
# # # #         model = Movie
# # # #         # fields = ["name_ch","movie_synopsis"]  # 指定字段
# # # #         # fields = "__all__"                       # 指定所有字段
# # # #         exclude = ["movie_synopsis"]
    
# # # # #===========查所有&添加数据# v1===========
# # # # class MovieAPIView(APIView):
# # # #     def get(self, request):
# # # #         movies_list = Movie.objects.all()
# # # #         serializer = MovieModelSerializer(instance=movies_list, many=True)
# # # #         # return HttpResponse(serializer.data)
# # # #         return Response(serializer.data)
    
# # # #     def post(self, request):
# # # #         # 数据校验
# # # #         serializer = MovieModelSerializer(data=request.data)
# # # #         if serializer.is_valid():
# # # #             # print('data', request.data)
# # # #             # Movie.objects.create(**serializer.validated_data)
# # # #             serializer.save()
# # # #             return Response(serializer.data)
# # # #         else:
# # # #             return Response(serializer.errors)
# # # # #===========查询一条,更新一条,删除一条
# # # # class MovieDetailAPIView(APIView):
# # # #     #===========查询一条
# # # #     def get(self, request, id):
# # # #         # movie_detail = Movie.objects.get(id=id)
# # # #         movie_detail = Movie.objects.filter(id=id).first()
# # # #         serializers = MovieModelSerializer(instance=movie_detail, many=False)
# # # #         return Response(serializers.data)
# # # #     #===========更新一条
# # # #     def post(self, request, id):
# # # #         update_data = Movie.objects.get(id=id)
# # # #         serializer = MovieModelSerializer(instance=update_data, data=request.data)
# # # #         if serializer.is_valid():
# # # #             # print("更新数据ing", serializer.validated_data)  # >> 更新数据ing OrderedDict([('name_ch', '千与千寻'), ('name_en', 'Spirited Away'), ('movie_synopsis', '更新数据')])
# # # #             # Movie.objects.filter(id=id).update(**serializer.validated_data)
# # # #             # update = Movie.objects.filter(id=id).first()
# # # #             # serializer.instance = update
# # # #             serializer.save()
# # # #             return Response(serializer.data)
# # # #         else:
# # # #             print("更新数据失败")
# # # #             return Response(serializer.errors)
# # # #     #===========删除一条
# # # #     def delete(self, request, id):
# # # #         Movie.objects.get(pk=id).delete()
# # # #         return Response()
# # # # ##############对一个表做五个接口，CRUD操作 END##############
# # # # ##############对一个表做五个接口，使用GenericAPIView##############
# # # # from rest_framework.generics import GenericAPIView

# # # #===========查所有&添加数据 v2#===========
# # # class MovieModelSerializer(serializers.ModelSerializer):
# # #     # description = serializers.CharField(source='movie_synopsis')
# # #     class Meta:
# # #         model = Movie
# # #         # fields = ["name_ch","movie_synopsis"]  # 指定字段
# # #         fields = "__all__"                       # 指定所有字段
# # #         # exclude = ["movie_synopsis"]
# # # class MovieView(GenericAPIView):
# # #     queryset = Movie.objects.all()
# # #     serializer_class = MovieModelSerializer

# # #     def get(self, request):
# # #         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
# # #         return Response(serializer.data)
# # #         # v3
# # #         # serializer = MovieModelSerializer(instance=self.get_queryset(), many=True)
# # #         # return Response(serializer.data)
# # #         # v2 
# # #         # movies_list = self.get_queryset()
# # #         # serializer = MovieModelSerializer(instance=self.movies_list, many=True)
# # #         # v1
# # #         # return HttpResponse(serializer.data)
    
# # #     def post(self, request):
# # #         serializer = self.get_serializer(data=request.data)
# # #         # 数据校验
# # #         if serializer.is_valid():
# # #             # print('data', request.data)
# # #             # Movie.objects.create(**serializer.validated_data)
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         else:
# # #             return Response(serializer.errors)

# # # #===========查询一条,更新一条,删除一条
# # # class MovieDetailView(GenericAPIView):
# # #     queryset = Movie.objects.all()
# # #     serializer_class = MovieModelSerializer
# # #     lookup_field = 'id'
# # #     #===========查询一条
# # #     def get(self, request, id):
# # #         serializers = self.get_serializer(instance=self.get_object(), many=False)
# # #         # movie_detail = Movie.objects.get(id=id)
# # #         # movie_detail = Movie.objects.filter(id=id).first()
# # #         # serializers = MovieModelSerializer(instance=movie_detail, many=False)
# # #         return Response(serializers.data)
# # #     #===========更新一条
# # #     def post(self, request, id):
# # #         serializer = self.get_serializer(instance=self.get_object(), data=request.data)

# # #         # update_data = Movie.objects.get(id=id)
# # #         # serializer = MovieModelSerializer(instance=update_data, data=request.data)
# # #         if serializer.is_valid():
# # #             # print("更新数据ing", serializer.validated_data)  # >> 更新数据ing OrderedDict([('name_ch', '千与千寻'), ('name_en', 'Spirited Away'), ('movie_synopsis', '更新数据')])
# # #             # Movie.objects.filter(id=id).update(**serializer.validated_data)
# # #             # update = Movie.objects.filter(id=id).first()
# # #             # serializer.instance = update
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         else:
# # #             print("更新数据失败")
# # #             return Response(serializer.errors)
# # #     #===========删除一条
# # #     def delete(self, request, id):
# # #         self.get_object().delete()
# # #         # Movie.objects.get(pk=id).delete()
# # #         return Response()



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
    