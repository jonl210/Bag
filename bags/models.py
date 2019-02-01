# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField()

class Bag(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item)
