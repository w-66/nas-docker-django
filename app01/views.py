from django.shortcuts import HttpResponse, render, redirect

from app01.models import Favormusic
from app01.models import Lifelog
from app01.models import App01Lifelog


from django.utils import timezone
# 导入自定义模块 雪花ID
from custom_modles import module_snowflake
#
def demo_test(request):
    content = '测试内容'
    return render(request, 'demo_test.html',{"content":content})
def demo_test01(request):
    return render(request, 'demo_test01.html')


def index(request):
    return render(request, 'index.html')

# 可用页面
##lifelog
def lifelog(request):
    if request.method == "GET":
        lifelog = App01Lifelog.objects.all().order_by("-addtime")[:40]
        return render(request, 'lifelog.html', {'lifelog':lifelog})

# ModelForm(实现添加日志信息)
from django import forms
from app01  import models



class LogModeForm(forms.ModelForm):
    class Meta:
        model = models.App01Lifelog # 获取表 
        # fields = ["addtime", "tag", "content", "weather", "location_id"]  # 获取表中的列
        fields = "__all__"                                       # 获取表中的所有列
    weather = forms.CharField(required=False)              # 取消input标签的required属性(默认所有inpute标签带有required属性)
        # widgets = {
        #     "addtime": forms.TextInput(attrs={"value": "2020"}),
        # }
    
    def __init__(self, *args, **kwargs):  # 定义input标签的class属性
        super().__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs = {"class": "form-control"}
            # 单独设置addtime项 默认值为当前日期时间
            if field[0] == "addtime":
                current_time = timezone.now()  # 获取当前时间
                field[1].widget.attrs = {"class": "form-control", "value": current_time}
            # 单独设置global_id
            elif field[0] == "global_id":
                worker = module_snowflake.IdWorker(1, 1, 0).get_id()  # 获取全局ID
                field[1].widget.attrs = {"class": "form-control", "value": worker}

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
        print('form.errors',"+++++form.errors的错误+++++")
        errors = form.errors
        return HttpResponse(errors)

class LifeLogEdit(forms.ModelForm):                            # 专门针对编辑的页面，去除了ID和添加时间的修改，不使用所有字段
    class Meta:
        model = models.App01Lifelog # 获取表 
        fields = ["tag", "content", "weather", "location_id"]  # 获取表中的列，专门针对编辑的页面，去除了ID和添加时间的修改
        # fields = "__all__"                                   # 获取表中的所有列
    weather = forms.CharField(required=False)                  # 取消input标签的required属性(默认所有inpute标签带有required属性)
        # widgets = {
        #     "addtime": forms.TextInput(attrs={"value": "2020"}),
        # }
    
    def __init__(self, *args, **kwargs):  # 定义input标签的class属性
        super().__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs = {"class": "form-control"}
            # 单独设置addtime项 默认值为当前日期时间
            if field[0] == "addtime":
                current_time = timezone.now()  # 获取当前时间
                field[1].widget.attrs = {"class": "form-control", "value": current_time}

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

def text(request):
    return render(request, 'text.html')

def learn_js_01(request):
    return render(request, 'learn_js_01.html')
    # return HttpResponse('JavaScript')
def learn_js_02(request):
    return render(request, 'learn_js_02.html')
def learn_js_03(request):
    return render(request, 'learn_js_03.html')
def learn_js_04(request):
    return render(request, 'learn_js_04.html')

def learn_react_01(request):
    return render(request, 'learn_react_01.html')
def learn_react_02(request):
    return render(request, 'learn_react_02.html')
def learn_react_03(request):
    return render(request, 'learn_react_03.html')
def learn_react_04(request):
    return render(request, 'learn_react_04.html')
def learn_react_05(request):
    return render(request, 'learn_react_05.html')
def learn_react_06(request):
    return render(request, 'learn_react_06.html')
def learn_react_07(request):
    return render(request, 'learn_react_07.html')
def learn_react_08(request):
    return render(request, 'learn_react_08.html')
def learn_react_09(request):
    return render(request, 'learn_react_09.html')
def learn_react_10(request):
    return render(request, 'learn_react_10.html')
def learn_react_11(request):
    return render(request, 'learn_react_11.html')
def learn_react_12(request):
    return render(request, 'learn_react_12.html')
def learn_react_13(request):
    return render(request, 'learn_react_13.html')
def learn_react_14(request):
    return render(request, 'learn_react_14.html')
def learn_react_15(request):
    return render(request, 'learn_react_15.html')
def learn_react_16(request):
    return render(request, 'learn_react_16.html')
def learn_react_17(request):
    return render(request, 'learn_react_17.html')

def learn_bootstrap_01(request):
    return render(request, 'learn_bootstrap_01.html')
def learn_bootstrap_02(request):
    return render(request, 'learn_bootstrap_02.html')
def learn_bootstrap_03(request):
    return render(request, 'learn_bootstrap_03.html')
def learn_bootstrap_04(request):
    return render(request, 'learn_bootstrap_04.html')
def learn_bootstrap_05(request):
    return render(request, 'learn_bootstrap_05.html')