"""Bag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#Import views from different apps
from home import views as home_views
from users import views as users_views
from bags import views as bags_views

urlpatterns = [
    url(r'^delete_bag', bags_views.delete_bag, name="delete_bag"),
    url(r'^bag/(?P<id>[0-9]+)/delete-bag', bags_views.delete_bag_view, name="delete_bag_view"),
    url(r'^delete_item', bags_views.delete_item, name="delete_item"),
    url(r'^items', users_views.all_items, name="all_items"),
    url(r'^bag/(?P<id>[0-9]+)/create_item', bags_views.create_item, name="create_item"),
    url(r'^bag/(?P<id>[0-9]+)/new-item', users_views.newitem_view, name="new_item"),
    url(r'^bag/(?P<id>[0-9]+)', users_views.bag, name="bag"),
    url(r'^bags', users_views.my_bags, name="my_bags"),
    url(r'^create_bag', bags_views.create_bag, name="create_bag"),
    url(r'^new-bag', users_views.newbag_view, name="new_bag"),
    url(r'^login_user', users_views.login_user, name="login_user"),
    url(r'^logout_user', users_views.logout_user, name="logout_user"),
    url(r'^signup_user', users_views.signup, name="signup_user"),
    url(r'^login', home_views.login_view, name="login_view"),
    url(r'^signup', home_views.signup_view, name="signup_view"),
    url(r'^$', home_views.index, name="index"),
    url(r'^admin/', admin.site.urls),
]
