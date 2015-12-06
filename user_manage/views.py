#!-*- coding:utf-8 -*-

import os
import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from .models import UserInfo
from .models import IpPortPassword 

def register(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('register.html', c)

def test(request):
    return HttpResponse("asdfasd;lfkjasd;lfj")

def submit_register(request):
    """
    name = request.POST['name']
    qq = request.POST['qq']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    """

    if len(request.POST['email'].strip()) == 0:
        return redirect('/user/register')

    try:
        user = get_object_or_404(UserInfo, 
                email = request.POST['email'].strip(' '))
    except Http404:
        user = create_user(request.POST)
        c = {}
        c['email'] =  user.email
        c['IP'] = user.delegate_ip
        c['PORT'] = user.delegate_port
        c['PASSWORD'] = user.delegate_password
        return render_to_response('list.html', c)
        #return HttpResponse("new user")
    else:
        c = {}
        c['name_value'] = request.POST['name']
        c['qq_value'] = request.POST['qq']
        c['email_value'] = request.POST['email']
        c['email_error'] = '该邮箱已注册，请重新输入...'
        c.update(csrf(request))
        return render_to_response('register.html', c)

def create_user(user_info):
    user = UserInfo(name = user_info['name'], qq = user_info['qq'], 
            email = user_info['email'], password = user_info['password'])
    ip_port = IpPortPassword.objects.filter(email = 'nouser')[0]
    ip_port.email = user.email
    user.delegate_ip = ip_port.ip
    user.delegate_port = ip_port.port
    user.delegate_password = ip_port.password
    ip_port.save()
    user.save()
    return user

def show_user_info(request):
    return render_to_response('user_info.html')

def show_login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def sub_login(request):
    #if email is empty, rediret to register
    if len(request.POST['email'].strip()) == 0:
        return redirect('/user/login')

    try:
        user = get_object_or_404(UserInfo, 
                email = request.POST['email'].strip(' '), password = request.POST['password'])
    except Http404:
        #not exist
        c = {}
        c.update(csrf(request))
        c['email_error'] = '用户名或密码错误，请重新输入...'
        c['email_value'] = request.POST['email']
        return render_to_response('login.html', c)
    else:
        c = {}
        #c.update(csrf(request))
        c['email'] =  user.email
        c['IP'] = user.delegate_ip
        c['PORT'] = user.delegate_port
        c['PASSWORD'] = user.delegate_password
        return render_to_response('list.html', c)
        #return render_to_response('userinfo.html', c)

def get_count(request):
    return render_to_response('list.html')

def initial(request):
    path = os.path.dirname(os.path.abspath(__file__)) + '/password_file.txt'
    f = open(path, 'r')
    encryption = f.readline()[10:21]

    count = 10
    for i in range(count):
        port = f.readline().strip()[5:]
        password = f.readline().strip()[9:]
        f.readline()

        record = IpPortPassword()
        record.ip = '54.254.209.180'
        record.port = int(port)
        record.password = password
        record.encryption = encryption
        record.save()
    return HttpResponse(os.path.dirname(os.path.abspath(__file__)) + str(count))
