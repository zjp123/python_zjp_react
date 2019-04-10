from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic import View
from reactperson.models import User
import datetime
from time import time
from django.contrib.auth import authenticate
# Create your views here.

class Login(View):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        # print(9999)
        isLogin = request.session.get('isLogin')
        if isLogin:
            return JsonResponse({'code': 200, 'message': '已登录', 'pathname': '/'})
        else:
            return HttpResponse()

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        # 接收参数
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 数据校验
        if not all([username, password]):
            return JsonResponse({'code': 401, 'message': '数据有误'})

        # 验证用户名
        user = authenticate(username=username, password=password)
        # try:
        #     user = User.objects.get(username=username, password=password)
        # except User.DoesNotExist:
        #
        #     user = None
        print(888)
        # print(user.id)
        if user:
            request.session['username'] = username
            request.session['isLogin'] = True
            access_start = datetime.datetime.now()
            access_start_str = access_start.strftime('%Y-%m-%d %H:%M:%S')
            request.session['loginTime'] = access_start_str
            return JsonResponse({'code': 200, 'message': '登录成功'})
        else:
            return JsonResponse({'code': 402, 'message': '用户名或密码错误'})





class register(View):

    @method_decorator(ensure_csrf_cookie)
    def get(self, request):

        print(9999)
        return HttpResponse()

    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        print(9999)

        # 获取参数
        username = request.POST.get('username')
        password = request.POST.get('password')

        confirmpassword = request.POST.get('confirmpassword')

        if password!=confirmpassword:
            return JsonResponse({'code': 402, 'message': '两次密码输入有误'})


        # 数据校验
        print(username, password, confirmpassword)

        if not all([username, password, confirmpassword]):

            return JsonResponse({'code': 401, 'message': '数据有误'})

        # 业务处理
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:

            user = None

        if not user:

            user = User.objects.create_user(username, '', password)
            user.is_active = 0
            user.save()
            print('uuuu')
            return JsonResponse({'code': 200, 'message': '注册成功'})


        else:

            return JsonResponse({'code': 206, 'message': '用户名已存在'})


class index(View):

    def get(self, request):
        print(9999)

        return JsonResponse({'code': 200, 'message': '这是首页'})


class api(View):
    def get(self, req):
        print(9999)

        return JsonResponse({'code': 200, 'message': 'ok'})
