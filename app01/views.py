from django.shortcuts import HttpResponse, render, redirect

from app01.models import Favormusic

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import requests
import re
import time

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
        # 获取POST数据
        c_song = request.POST.get('c_song')
        c_songer = request.POST.get('c_songer')
        c_album = request.POST.get('c_album')
        # 
        Favormusic.objects.filter(global_id=global_id).update(song=c_song, songer=c_songer, album=c_album)
        # 修改完成之后 重定向到音乐列表页面
        return redirect('http://qwertyui.vip:22280/music/list/')

def crawler_music(request):
    '''手动爬虫任务'''

    wangyiyun_music_list_predownload = 'https://music.163.com/#/playlist?id=7624041147'   # 预下载
    # selenium获取歌单
    songList = get_html_selenium(wangyiyun_music_list_predownload)

    # return HttpResponse('ca')
    return HttpResponse(songList)


# 内部调用
def get_html_selenium(wangyiyun_music_list_predownload):
    '''
    : wangyiyun_music_list_predownload : 歌单链接
    : return : 歌曲信息列表(包含: 歌手 歌名 时长 专辑 歌曲ID)
    '''

    chrome_option = webdriver.ChromeOptions()
    # # 隐藏浏览器的窗口
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--no-sandbox')
    chrome_option.add_argument('--disable-gpu')
    chrome_option.add_argument('--disable-dev-shm-usage')

    # ua
    chrome_option.add_argument('--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36')
    # 因为报错，浏览器要求您接受网站的证书。您可以设置默认情况下忽略这些错误，以免发生这些错误。 
    #   [15896:15424:1004/210056.030:ERROR:ssl_client_socket_impl.cc(983)] handshake failed; returned -1, SSL error code 1, net_error -101
    chrome_option.add_argument('-ignore-certificate-errors')
    chrome_option.add_argument('-ignore -ssl-errors')
    # 创建实例
    s = Service(executable_path='/usr/local/bin/chromedriver')
    browser = webdriver.Chrome(service=s, options=chrome_option)
    browser.get(wangyiyun_music_list_predownload)

    # 切换 frame
    browser.switch_to.frame('g_iframe')
    print('已切换frame至g_iframe'.center(50, '-'))

    # 设置等待时间
    # import time
    # time.sleep(4)
    browser.implicitly_wait(10)

    # 定位元素
    singers = browser.find_elements(By.CSS_SELECTOR, '#song-list-pre-cache>div>div>table>tbody>tr>td>div.text>span')  # 歌手; 成功，终于可以了，我去2022_10_05 
    songs_name = browser.find_elements(By.CSS_SELECTOR, '#song-list-pre-cache>div>div>table>tbody>tr>td>div>div>div>span.txt>a>b')  # 歌名
    durations = browser.find_elements(By.CSS_SELECTOR, '#song-list-pre-cache>div>div>table>tbody>tr>td>span.u-dur ')  # 时长
    albums = browser.find_elements(By.CSS_SELECTOR, '#song-list-pre-cache>div>div>table>tbody>tr>td>div.text>a')  # 专辑名称
    songids = browser.find_elements(By.CSS_SELECTOR, '#song-list-pre-cache>div>div>table>tbody>tr>td>div>div>div>span.txt>a') # 网易的歌曲ID

    singersList = []
    songs_name_List = []
    durationList = []
    albumsList = []
    songidsList = []

    # 获取歌手名称
    for singer in singers:
        # print(singer.get_attribute('title'))  # 成功
        singersList.append(singer.get_attribute('title'))
        # singersList.append(unicodedata.normalize('NFKC', singer.get_attribute('title')))
    # # 获取歌名
    for song_name in songs_name:
        # print(song_name.get_attribute('title'))  # 成功
        song_name_ASCII = ' '.join(song_name.get_attribute('title').split()) # 去除字符中的\xa0 不间断空白符 &nbsp; 我们通常所用的空格是 \x20 ，是在标准ASCII可见字符 0x20~0x7e 范围内。 
        songs_name_List.append(song_name_ASCII)
    # 获取时长
    for duration in durations:
        # print(duration.text)
        durationList.append((duration.text))
    # 获取专辑名称
    for album in albums:
        # print(album.get_attribute('title'))
        song_name_ASCII = ' '.join(album.get_attribute('title').split())
        # albumsList.append(album.get_attribute('title'))
        albumsList.append(song_name_ASCII)
    # print(albumsList)
    # 获取歌曲ID
    for songid in  songids:
        link = songid.get_attribute('href')  # /song?id=1384132124
        # print(link)
        getid = re.search(r'(https://music.163.com/song\?id=)([0-9]{4,12})(.*)', link)  # 提取id 取第2组
        # print(getid.group(2))
        songidsList.append(getid.group(2))

    # 合并列表
    songs = [x for x in zip(singersList, songs_name_List, durationList, albumsList, songidsList)]
    # print(songs)

    return songs
