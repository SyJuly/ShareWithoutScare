# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def friends(request):
    return render(request, 'friends.html')