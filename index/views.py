#!-*- coding:utf-8 -*-

import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)
