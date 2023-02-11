from django.shortcuts import HttpResponse, render, redirect
from app01  import models 
from app01.models import App01Lifelog
from app01.utils.form import LogModeForm, LifeLogEdit

#lifelog 查看
## lifelog的搜索功能(暂时为只能搜索内容)20230207
def lifelog(request):
    ### 创建空字典，存储get请求的数据
    data_dict = {}
    search_data = request.GET.get('s','')  # 后面的空值，没看到啥用啊，有没有都一样，只是在判断的时候，添加到字典一个空值?
    ### 判断通过get传过来的值是否为空，不为空，则添加到字典中
    if search_data:
        data_dict['content__contains'] = search_data
    
    ### 分页操作
    #### 方式二 定义类，使用对象来生成页码
    #### 通过字典的内容进行数据库查询
    queryset = models.App01Lifelog.objects.filter(**data_dict).order_by("-addtime")

    from app01.utils.pagination import Pagination 
    obj_page = Pagination(request, queryset, subsection=3, page_limit=6)     #创建对象实例 

    return render(request, 'lifelog.html', 
                  {'queryset':obj_page.one_page_queryset , 'page_count':obj_page.page_count, 'page_up':obj_page.page-1, 'page_down':obj_page.page+1, 'search_data':search_data, 'page_Num_HTML':obj_page.page_num_html()})



def lifelog_log(request):
    # ModeForm (Django)
    if request.method == "GET":
        form = LogModeForm()  # 创建LogModeForm的实例对象
        return render(request, 'lifelog_log.html',{"form":form})  # 传到模板中
    
    # 用户POST提交数据，数据校验
    form = LogModeForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库中
        # print(form.cleaned_data)
        form.save()        # 如果数据是有效的，存入之前获取的表中
        return redirect('/lifelog/')
    else:
        errors = form.errors
        return HttpResponse(errors)


def lifelog_edit(request,global_id):                                      # 编辑记录
    # one_row = App01Lifelog.objects.filter(global_id=global_id).first()  # 获取数据方式一(教程中的方式)
    one_row = App01Lifelog.objects.get(global_id=global_id)               # 获取数据方式二 <one_row复用>
    if request.method == "GET":
        form = LifeLogEdit(instance=one_row)                              ## 复用处1
        # return render(request, 'lifelog_edit.html', {'onerow':one_row,'global_id':global_id})
        return render(request, 'lifelog_edit.html', {'form':form})
    
    form = LifeLogEdit(data=request.POST, instance=one_row)               ## 复用处2
    if form.is_valid():    # 校验提交的数据 
        form.save()
        return redirect('/lifelog/')
    return render(request, 'lifelog_edit.html', {'form':form})

def lifelog_del(request, global_id):
    App01Lifelog.objects.filter(global_id=global_id).delete()
    return redirect('/lifelog/')

