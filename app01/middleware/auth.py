from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class Auth(MiddlewareMixin):
    def process_request(self, request):
        # 判断是否是login页面，如果是，则不作操作
        if request.path in {'/login/', '/auth/code/', '/index/', 'learn/'}:
            return
        # 否则就验证用户session是否存在
        info_dict = request.session.get("info")
        # 如果存在，则访问对应页面
        if info_dict:
            return
        # 不然重定向到login页面
        return redirect("/login/")
