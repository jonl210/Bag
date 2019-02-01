# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Bag, Item
from users.models import Profile

#Import requests and BeautifulSoup to fetch page title
import requests
import bs4

#Create a new bag
def create_bag(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        new_bag = Bag.objects.create(name=request.POST["name"])
        profile.bags.add(new_bag)
        return redirect("my_bags")

#Delete bag view
def delete_bag_view(request, id):
    bag = Bag.objects.get(id=id)
    return render(request, "users/delete_bag.html", {"bag": bag})

#Delete bag
def delete_bag(request):
    if request.method == "POST":
        bag = Bag.objects.get(id=request.POST["bag_id"])
        items = bag.items.all()

        #Delete all items in bag
        for item in items:
            item.delete()

        #Delete bag
        bag.delete()

        return redirect("my_bags")

#Create a new item and add it to the bag
def create_item(request, id):
    if request.method == "POST":
        bag = Bag.objects.get(id=id)

        if request.POST["title"] == "":
            title = get_url_title(request.POST["url"]) #Fetch title
            new_item = Item.objects.create(url=request.POST["url"], name=title)
        else:
            new_item = Item.objects.create(url=request.POST["url"], name=request.POST["title"])
        bag.items.add(new_item)
        return redirect("bag", id)

#Delete an item
def delete_item(request):
    if request.method == "POST":
        item = Item.objects.get(id=request.POST["item_id"])
        item.delete()
        return redirect("bag", request.POST["bag_id"])

#Get the title of the web page
def get_url_title(url):
    r = requests.get(url, timeout=5)
    html = bs4.BeautifulSoup(r.text)
    title = html.title.text
    return title
