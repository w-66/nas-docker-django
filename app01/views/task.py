import json
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01.models import Task

from app01.utils.pagination import Pagination 
from app01.utils.form import Task_add_ModeForm


form_title = "新建任务"
# 接收ajax请求
@csrf_exempt
def task_ajax(request):
    # print('request', request)
    # print('request.session', request.session)
    # 创建空字典，存储get请求的数据
    data_dict = {}
    search_data = request.GET.get('s','')  # 后面的空值，没看到啥用啊，有没有都一样，只是在判断的时候，添加到字典一个空值?
    ### 判断通过get传过来的值是否为空，不为空，则添加到字典中
    if search_data:
        data_dict['username__contains'] = search_data
    queryset = Task.objects.filter(**data_dict).order_by("id")

    obj_page = Pagination(request, queryset, subsection=3, page_limit=6)     #创建对象实例 
    
    # 创建表单，通过ajax提交数据
    form = Task_add_ModeForm()  # 创建Task_add_ModeForm的实例对象
    
    return render(request, 'task.html', {"form_title":form_title,
        'queryset':obj_page.one_page_queryset,
        'page_count':obj_page.page_count, 
        'page_up':obj_page.page-1, 
        'page_down':obj_page.page+1, 
        'search_data':search_data, 
        'page_Num_HTML':obj_page.page_num_html(),
        'form':form
        })

@csrf_exempt
def task_ajax_add(request):
    print('通过ajsx发送过来的post信息:', request.POST)
    data_dict = {'status': True, 'info':'123'}
    return HttpResponse(json.dumps(data_dict))

    
    # form_title = "新建任务"
    # if request.method == "GET":
    #     form = Task_add_ModeForm()  # 创建Task_add_ModeForm的实例对象
    #     return render(request, 'ajax_form_add.html',{"form":form, 'form_title':form_title})  # 传到模板中
    
    # # 用户POST提交数据，数据校验
    # form = Task_add_ModeForm(data=request.POST)
    # if form.is_valid():
    #     # 如果数据合法，保存到数据库中
    #     form.save()        # 如果数据是有效的，存入之前获取的表中
    #     return redirect('/task/')
    # return render(request, 'ajax_form_add.html',{"form":form, 'form_title':form_title})  # 传到模板中

    # print(request.POST)
    # data_dict = {"status":True, "data": [12, 1]}
    # return HttpResponse(json.dumps(data_dict))

def task_edit(request, id):
    title = '任务信息编辑'
    one_row = Task.objects.filter(id=id).first()               # 获取数据方式二 <one_row复用>
    
    # 判断编辑的信息是否存在，不存在则返回错误信息页面
    if not one_row:
        error = '编辑的信息不存在'
        return render(request, 'error.html', {'error':error})
    
    if request.method == "GET":
        form = Task_add_ModeForm(instance=one_row)  # 创建Task_add_ModeForm的实例对象
        return render(request, 'form_edit.html', {'form':form,'title':title})

    # 用户POST提交数据，数据校验
    form = Task_add_ModeForm(data=request.POST, instance=one_row)
    if form.is_valid():
        # 如果数据合法，保存到数据库中
        form.save()        # 如果数据是有效的，存入之前获取的表中
        return redirect('/admin/')
    return render(request, 'ajax_form_add.html',{"form":form, 'form_title':'新建管理员'})  # 传到模板中
