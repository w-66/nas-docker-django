from django.shortcuts import render, redirect, HttpResponse

def demo_uploadfile(request):
    if request.method == "GET":
        return render(request, 'demo_uploadfile.html')
    if request.method == "POST":
        print(request.POST)   # <QueryDict: {'csrfmiddlewaretoken': ['NDYD6qMgj6hK1QXCCmfhbPCVja5xB1A0lOZxpjsHEw1crFhW7sFWaWmL5HLGRrfn'], 'file_info': ['123']}>
        # HTML的input所在的form标签中需要添加属性: 'enctype="multipart/form-data"'才能上传文件
        print(request.FILES)  # <MultiValueDict: {'file': [<InMemoryUploadedFile: 0.png (image/png)>]}>
        obj_file = request.FILES.get('file')
        # print(obj_file)       # 获取文件名: 0.png

        path = f"/www/django_www/tmp/{obj_file}"
        with open(path, mode='wb') as f:  
            for chunk in obj_file.chunks():  
                f.write(chunk) 
        return HttpResponse('123')
    


    



