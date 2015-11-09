#!-*- coding:utf-8 -*-

import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from .models import UserInfo

def register(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('register.html', c)

def submit_register(request):
    """
    name = request.POST['name']
    qq = request.POST['qq']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    """

    try:
        user = get_object_or_404(UserInfo, email = request.POST['email'])
    except Http404:
        create_user(request.POST)
        return HttpResponse("new user")
    else:
        return HttpResponse("user exist")

def create_user(user_info):
    user = UserInfo(name = user_info['name'], qq = user_info['qq'], 
                    email = user_info['email'], password = user_info['password'])
    user.save()
