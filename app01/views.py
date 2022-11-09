from django.shortcuts import HttpResponse, render, redirect
from app01.models import Favormusic

def demo_text(request):
    return HttpResponse('text')
def music_list(request):
    '''favor music list'''

    # 取出查询的所有数据
    musicobj = Favormusic.objects.all().order_by("-addtime")
    return render(request, 'music_list.html', {'musicobj':musicobj})

def music_list_edit(request, global_id):
    '''修改歌曲信息'''
    if request.method == "GET":
        rowobj = Favormusic.objects.filter(global_id=global_id).first()
        return render(request, 'music_list_edit.html', {'rowobj':rowobj})
    else:
        # UserInfo.objects.filter(id=13).update(password='aaaa')
        c_song = request.POST.get('c_song')
        c_songer = request.POST.get('c_songer')
        c_album = request.POST.get('c_album')
        Favormusic.objects.filter(global_id=global_id).update(song=c_song, songer=c_songer, album=c_album)
        return redirect('http://qwertyui.vip:22280/music/list/')

def crawler_music(request):
    '''手动爬虫任务'''
    return HttpResponse('crawler music')