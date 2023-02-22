import json
from django.shortcuts import HttpResponse, render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01  import models 
from app01.models import App01Lifelog
from app01.utils.form import LogModeForm, LogModeForm_exclude
from app01.utils.pagination import Pagination 
# #雪花ID
from custom_modles import module_snowflake


def lifelog_v2(request):
    title = '添加记录'
    ### 创建空字典，存储get请求的数据
    data_dict = {}
    search_data = request.GET.get('s','')  # 后面的空值，没看到啥用啊，有没有都一样，只是在判断的时候，添加到字典一个空值?
    ### 判断通过get传过来的值是否为空，不为空，则添加到字典中
    if search_data:
        data_dict['content__contains'] = search_data

    ### 分页操作
    #### 通过字典的内容进行数据库查询
    queryset = models.App01Lifelog.objects.filter(**data_dict).order_by("-addtime")
    obj_page = Pagination(request, queryset, subsection=3, page_limit=6)     #创建对象实例 


    if request.method == "GET":
        form = LogModeForm_exclude()
        return render(request, 'lifelog_v2.html', 
                      {'form':form, 
                       'form_title':title,
                       'queryset':obj_page.one_page_queryset , 
                       'page_count':obj_page.page_count, 
                       'page_up':obj_page.page-1, 
                       'page_down':obj_page.page+1, 
                       'search_data':search_data, 
                       'page_Num_HTML':obj_page.page_num_html()
                       })

    
@csrf_exempt
def lifelog_v2_add_ajax(request):
    form = LogModeForm_exclude(data=request.POST)
    if form.is_valid():
        # 自动生成id，去调前端的输入，由系统自动生成
        form.instance.global_id = module_snowflake.IdWorker(1, 1, 0).get_id()
        form.save()
        data_dict = {'status': True}
        return HttpResponse(json.dumps(data_dict))
    
    data_dict = {'status': False, 'errors':form.errors}
    return JsonResponse(data_dict)

def lifelog_v2_del(request, global_id):
    App01Lifelog.objects.filter(global_id=global_id).delete()
    return redirect('/lifelog/v2/')