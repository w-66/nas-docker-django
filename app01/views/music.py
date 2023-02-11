from django.shortcuts import render,redirect
from app01.models import Favormusic

##music
def music_list(request):
    '''favor music list'''
    # 取出查询的所有数据
    musicobj = Favormusic.objects.using('second_db').all().order_by("-addtime")[:40]
    return render(request, 'music_list.html', {'musicobj':musicobj})

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