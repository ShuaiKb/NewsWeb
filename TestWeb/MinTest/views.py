from django.shortcuts import render, redirect

import re
import  os
from MinTest.models import User
from MinTest.models import News
from MinTest.models import Message
from TestWeb.settings import STATICFILES_DIRS
from lib.lib import my_md5
from django.conf import settings
from django.core.mail import send_mail
import random
from utils import sms
from django.shortcuts import HttpResponse
from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime


# 将请求定位到index.html文件中
def index3d(request):
    return render(request, 'index3d.html')

def userinform(request):
    if request.session.get('username'):
        user = User.objects.get(username=request.session.get('username'))
        if user:
            return render(request, 'userinform.html',locals())
def time(request):
    return render(request, 'time.html')

def index(request):
    if request.session.get('username'):
        user = User.objects.get(username=request.session.get('username'))
        if user:
            return render(request,'index.html',locals())
    if request.method == 'GET':
        return render(request, 'index3d.html')
def mindex1(request):
    if request.session.get('username'):
        news = News.objects.filter(classes=1)
        pagenum = request.GET.get('pagenum')
        if(pagenum==None):
            pagenum=2;
        paginator = Paginator(news, 10)
        try:
            post = paginator.page(pagenum)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(1)
        mess = Message.objects.filter(classes=1).order_by('-id')
        post.classes_id = 1
        return render(request, 'mindex.html', locals())
    else:
        return redirect('/zhuye/login/')
def mindex2(request):
    if request.session.get('username'):
        news = News.objects.filter(classes=2)
        pagenum = request.GET.get('pagenum')
        if(pagenum==None):
            pagenum=2;
        paginator = Paginator(news, 10)
        try:
            post = paginator.page(pagenum)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(1)
        mess = Message.objects.filter(classes=2).order_by('-id')
        post.classes = 2
        return render(request, 'mindex.html', locals())
    else:
        return redirect('/zhuye/login/')
def mindex3(request):
    if request.session.get('username'):
        news = News.objects.filter(classes=3)
        pagenum = request.GET.get('pagenum')
        if(pagenum==None):
            pagenum=2;
        paginator = Paginator(news, 10)
        try:
            post = paginator.page(pagenum)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(1)
            mess = Message.objects.filter(classes=3).order_by('-id')
        post.classes = 3
        return render(request, 'mindex.html', locals())
    else:
        return redirect('/zhuye/login/')
def mindex4(request):
    if request.session.get('username'):
        news = News.objects.filter(classes=4)
        pagenum = request.GET.get('pagenum')
        if(pagenum==None):
            pagenum=2;
        paginator = Paginator(news, 10)

        try:
            post = paginator.page(pagenum)
        except PageNotAnInteger:
            post = paginator.page(1)

        except EmptyPage:
            post = paginator.page(1)
        mess = Message.objects.filter(classes=4).order_by('-id')
        post.classes = 4
        return render(request, 'mindex.html', locals())
    else:
        return redirect('/zhuye/login/')
def mindex5(request):
    if request.session.get('username'):
        news = News.objects.filter(classes=5)
        pagenum = request.GET.get('pagenum')
        if(pagenum==None):
            pagenum=2;
        paginator = Paginator(news, 10)
        try:
            post = paginator.page(pagenum)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(1)
        mess = Message.objects.filter(classes=5).order_by('-id')
        post.classes = 5
        return render(request, 'mindex.html', locals())
    else:
        return redirect('/zhuye/login/')

def welcome(request):
    return render(request,'welcome.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       rs = User.objects.filter(username=username,password=my_md5(password))
       if rs:
           request.session['username'] = username
           request.session['userid'] = rs[0].id
           return redirect('/zhuye/index/')
def registe_sms(request):
    if request.method == 'GET':
        return render(request, 'registe_sms.html')
    if request.method == 'POST':
        if request.POST.get('mobile') and request.POST.get('code')==None:
            if not re.match(r"^1[35678]\d{9}$", request.POST.get('mobile')):
                message = "请输入正确的手机号码！"
                return redirect(request, 'registe_sms.html', locals())
            mobile = "86" + str(request.POST.get('mobile'))
            msg = str(random.randint(100000, 1000000))
            cache.set(mobile, msg, 60 * 3)
            sms.send(mobile, msg, '5')
            return render(request, 'registe_sms.html')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mobile ="86"+ request.POST.get('mobile')
        code = request.POST.get('code')
        message =''
        if username == None:
            message = "用户名不能为空！"
            return render(request, 'registe_sms.html', locals())
        if password1 == None or password2 == None:
            message = "密码不能为空！"
            return render(request, 'registe_sms.html', locals())
        if username == None:
            message = "手机号不能为空！"
            return render(request, 'registe_sms.html', locals())
        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'registe_sms.html', locals())
        else:
            same_name_user = User.objects.filter(username=username)
            if same_name_user:  # 用户名唯一
                message = '用户名已经存在！'
                return render(request, 'registe_sms.html', locals())
            same_mobile_user = User.objects.filter(mobile=mobile)
            if same_mobile_user:
                message = '该手机号码已被注册！'
                return render(request, 'registe_sms.html', locals())
            if cache.get(mobile) and cache.get(mobile) == code:
                new_user = User.objects.create()
                new_user.username = username
                new_user.password = my_md5(password1)  # 使用加密密码
                new_user.mobile = mobile
                new_user.save()
                return redirect('/zhuye/login/')
            else:
                message = '验证码已过期！'
                return render(request, 'registe_sms.html', locals())
def registe_mail(request):
    if request.method == 'GET':
        return render(request, 'registe_mail.html')
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('code')==None:
            email = str(request.POST.get('email'))
            same_email_user = User.objects.filter(email=email)
            msg1 = str(random.randint(100000, 1000000))
            cache.set(email, msg1, 60 * 1)
            msg = "尊敬的望尽阑珊用户：\n您好\n你的注册验证码为:" + msg1
            send_mail(
                '您的验证码请注意查收',
                msg,
                settings.EMAIL_HOST_USER,
                [email],
            )
            return render(request, 'registe_mail.html')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        code = request.POST.get('code')
        message =''
        if username == None:
            message = "用户名不能为空！"
            return render(request, 'registe_mail.html', locals())
        if password1 == None or password2 == None:
            message = "密码不能为空！"
            return render(request, 'registe_mail.html', locals())
        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'registe_mail.html', locals())
        else:
            same_name_user = User.objects.filter(username=username)
            if same_name_user:  # 用户名唯一
                message = '用户名已经存在！'
                return render(request, 'registe_mail.html', locals())
            my_emali = re.findall(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{2,3}$', email)
            if not my_emali:
                message = '请输入正确邮箱！'
                return redirect(request, 'registe_mail.html', locals())
            same_email_user = User.objects.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = '该邮箱地址已被注册！'
                return render(request, 'registe_mail.html', locals())
            if cache.get(email) and cache.get(email) == code:
                new_user = User.objects.create()
                new_user.username = username
                new_user.password = my_md5(password1)  # 使用加密密码
                new_user.email = email
                new_user.save()
                return redirect('/zhuye/login/')
            else:
                message = '验证码已过期！'
                return render(request, 'registe_mail.html', locals())
def exit(request):
    del request.session['username']
    del request.session['userid']
    return render(request,'login.html')
def exit1(request):
    del request.session['username']
    del request.session['userid']
    return render(request,'login.html')
def liuyan(request):
    if request.method == 'POST':
        timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username=request.session.get('username')
        img=User.objects.values("userinfo").filter(username=request.session.get('username'))
        content=request.POST.get('content')
        classes = request.POST.get('classes')
        if img:
            new_message = Message.objects.create()
            new_message.name=username
            new_message.time=timenow
            new_message.img=img
            new_message.content = content
            new_message.classes = classes
            new_message.save()
            return redirect('/mindex%s/'%classes)
def admin_list(request):
    return render(request, 'admin-list.html')
def news_list(request):
    if request.session.get('username'):
        news = News.objects.all()
        number =News.objects.all().count()
        pagenum = request.GET.get('pagenum')
        if(pagenum==None):
            pagenum=2;
        paginator = Paginator(news, 23)
        try:
            post = paginator.page(pagenum)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(1)
        return render(request, 'news-list.html',locals())
def test_add(request):
    if request.method == "GET":
        return render(request, "test-add.html", locals())
    if request.method == "POST":
        articletitle = request.POST.get('articletitle')
        articletype = request.POST.get('articletype')
        author = request.POST.get('author')
        sources = request.POST.get('sources')
        content = request.POST.get('content')
        timenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fp = request.FILES.get("file")
        img ="img/new_%s/"%articletype+fp.name
        print(articletitle,articletype,author,sources,content,img)
        print(type(articletype))
        print(articletype)
        error = ""
        # fp 获取到的上传文件对象
        if fp:
            path = os.path.join(STATICFILES_DIRS[0], 'img/new_%s/'%articletype + fp.name)  # 上传文件本地保存路径， image是static文件夹下专门存放图片的文件夹
            # fp.name #文件名
            # yield = fp.chunks() # 流式获取文件内容
            # fp.read() # 直接读取文件内容
            if fp.multiple_chunks():  # 判断上传文件大于2.5MB的大文件
                # 为真
                file_yield = fp.chunks()  # 迭代写入文件
                with open(path, 'wb') as f:
                    for buf in file_yield:  # for情况执行无误才执行 else
                        f.write(buf)
                    else:
                        print("大文件上传完毕")
            else:
                with open(path, 'wb') as f:
                    f.write(fp.read())
                print("小文件上传完毕")
        else:
            error = "文件上传为空"
            return render(request, "test-add.html", locals())
        new = News.objects.create()
        new.title = articletitle
        new.classes = articletype
        new.time = timenow
        new.content = content
        new.img = img
        new.author = author
        new.save()
        print("入库成功")
        return redirect("/zhuye/news_list/")
# def send_qqmail(request):
#     if request.method == 'GET':
#         return render(request, 'mailtest.html')
#     if request.POST.get('code') and request.POST.get('mobile'):
#         mobile = request.POST.get('mobile')
#         code = request.POST.get('code')
#         if cache.has_key(mobile) and cache.get(mobile) == code:
#             return HttpResponse("ok")
#         else:
#             return HttpResponse("验证码已过期")
#     else:
#         number = str(request.POST.get('mobile'))
#         msg1 = str(random.randint(100000, 1000000))
#         cache.set(number, msg1, 60 * 3)
#         print(number)
#         msg = "尊敬的望尽阑珊用户：\n您好\n你的注册验证码为:" + msg1
#         send_mail(
#             '您的验证码请注意查收',
#             msg,
#             settings.EMAIL_HOST_USER,
#             [number],
#         )
#         return render(request, 'mailtest.html')

#
# def send_qqsms(request):
#     if request.POST.get('mobile'):
#         number = "86"+str(request.POST.get('mobile'))
#         msg = str(random.randint(100000, 1000000))
#         sms.send(number, msg, '5')
#         return render(request, 'smstest.html')
#     else:
#         return render(request, 'smstest.html')
