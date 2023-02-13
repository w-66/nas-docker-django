from django.shortcuts import render,redirect
from app01.models import Favormusic

from app01.utils.pagination import Pagination 

##music
def music_list(request):
    '''favor music list'''
    # 取出查询的所有数据
        # 创建空字典，存储get请求的数据
    data_dict = {}
    search_data = request.GET.get('s','')  # 后面的空值，没看到啥用啊，有没有都一样，只是在判断的时候，添加到字典一个空值?
    ### 判断通过get传过来的值是否为空，不为空，则添加到字典中
    if search_data:
        data_dict['song__contains'] = search_data
    # user_list = Admin.objects.using('second_db').all().order_by("-addtime")[:40]
    queryset = Favormusic.objects.using('second_db').filter(**data_dict).order_by("-addtime")

    # musicobj = Favormusic.objects.using('second_db').all().order_by("-addtime")[:40]
    obj_page = Pagination(request, queryset, subsection=3, page_limit=9)     #创建对象实例 
    # return render(request, 'music_list.html', {'musicobj':musicobj})
    return render(request, 'music_list.html', {
        'queryset':obj_page.one_page_queryset,
        'page_count':obj_page.page_count, 
        'page_up':obj_page.page-1, 
        'page_down':obj_page.page+1, 
        'search_data':search_data, 
        'page_Num_HTML':obj_page.page_num_html()
        })


def music_list_edit(request, global_id):
    '''修改歌曲信息'''
    if request.method == "GET":
        """GET请求 访问歌曲编辑页面"""
        rowobj = Favormusic.objects.using('second_db').filter(global_id=global_id).first()
        return render(request, 'music_list_edit.html', {'rowobj':rowobj,'global_id':global_id})
    else:
        """POST请求 提交修改的数据到数据库"""
        # 获取POST数据
        c_song = request.POST.get('c_song')
        c_songer = request.POST.get('c_songer')
        c_album = request.POST.get('c_album')
        c_tag = request.POST.get('c_tag')
        # 
        Favormusic.objects.using('second_db').filter(global_id=global_id).update(song=c_song, songer=c_songer, album=c_album, tag=c_tag)
        # 修改完成之后 重定向到音乐列表页面
        return redirect('/music/list/')
    
