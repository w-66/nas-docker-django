from django.shortcuts import render, redirect, HttpResponse
from app01.models import Admin

from app01.utils.pagination import Pagination 
from app01.utils.form import Admin_add_ModeForm


def admin(request):
    # print('request', request)
    # print('request.session', request.session)

    # 创建空字典，存储get请求的数据
    data_dict = {}
    search_data = request.GET.get('s','')  # 后面的空值，没看到啥用啊，有没有都一样，只是在判断的时候，添加到字典一个空值?
    ### 判断通过get传过来的值是否为空，不为空，则添加到字典中
    if search_data:
        data_dict['username__contains'] = search_data
    queryset = Admin.objects.filter(**data_dict).order_by("id")

    obj_page = Pagination(request, queryset, subsection=3, page_limit=6)     #创建对象实例 
    return render(request, 'admin.html', {
        'queryset':obj_page.one_page_queryset,
        'page_count':obj_page.page_count, 
        'page_up':obj_page.page-1, 
        'page_down':obj_page.page+1, 
        'search_data':search_data, 
        'page_Num_HTML':obj_page.page_num_html()
        })

def admin_add(request):
    if request.method == "GET":
        form = Admin_add_ModeForm()  # 创建Admin_add_ModeForm的实例对象
        return render(request, 'form_add.html',{"form":form, 'form_title':'新建管理员'})  # 传到模板中
    
    # 用户POST提交数据，数据校验
    form = Admin_add_ModeForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库中
        form.save()        # 如果数据是有效的，存入之前获取的表中
        return redirect('/admin/')
    return render(request, 'form_add.html',{"form":form, 'form_title':'新建管理员'})  # 传到模板中

def admin_edit(request, id):
    title = '管理员信息编辑'
    one_row = Admin.objects.filter(id=id).first()               # 获取数据方式二 <one_row复用>
    
    # 判断编辑的信息是否存在，不存在则返回错误信息页面
    if not one_row:
        error = '编辑的信息不存在'
        return render(request, 'error.html', {'error':error})
    
    if request.method == "GET":
        form = Admin_add_ModeForm(instance=one_row)  # 创建Admin_add_ModeForm的实例对象
        return render(request, 'form_edit.html', {'form':form,'title':title})

    # 用户POST提交数据，数据校验
    form = Admin_add_ModeForm(data=request.POST, instance=one_row)
    if form.is_valid():
        # 如果数据合法，保存到数据库中
        form.save()        # 如果数据是有效的，存入之前获取的表中
        return redirect('/admin/')
    return render(request, 'form_add.html',{"form":form, 'form_title':'新建管理员'})  # 传到模板中

def admin_del(request, id):
    Admin.objects.filter(id=id).delete()
    return redirect('/admin/')