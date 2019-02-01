# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from forms import SignUpForm
from models import Profile
from bags.models import Bag, Item

#Sign up new user
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            new_user = User.objects.create_user(username, email, password)
            Profile.objects.create(user=new_user)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
        else:
            return redirect("signup_view")

#Log out user
def logout_user(request):
    logout(request)
    return redirect("index")

#Log in user
def login_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return redirect("login_view")

#New bag view
def newbag_view(request):
    return render(request, "users/newbag.html")

#New item view
def newitem_view(request, id):
    bag = Bag.objects.get(id=id)
    return render(request, "users/newitem.html", {"bag":bag})

#Display all of users bags
def my_bags(request):
    profile = Profile.objects.get(user=request.user)
    bags = profile.bags.all()
    return render(request, "users/mybags.html", {"bags":bags})

#Display all items from every bag
def all_items(request):
    all_items = []
    profile = Profile.objects.get(user=request.user)
    bags = profile.bags.all()

    #Iterate through each bag and get all items
    #then add to all_items list
    for bag in bags:
        items = bag.items.all()
        for item in items:
            all_items.append(item)

    return render(request, "users/allitems.html", {"items":all_items})

#Display a bag and all items within
@login_required
def bag(request, id):
    bag = Bag.objects.get(id=id)
    creator = bag.profile_set.all().first().user #Get creator of bag

    if(request.user == creator):
        items = bag.items.all()
        return render(request, "users/bag.html", {"bag":bag, "items":items})
    else:
        return redirect("index")
