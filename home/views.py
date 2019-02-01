# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#Render home page(if user is not logged in)
def index(request):
    if request.user.is_authenticated:
        return render(request, "home/layout.html")
    else:
        return render(request, "home/home.html")

#Sign up view
def signup_view(request):
    return render(request, "home/signup.html")

#Log in view
def login_view(request):
    return render(request, "home/login.html")
