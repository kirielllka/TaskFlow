from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    category_name = models.CharField(blank=False, verbose_name="name")
    created_user = models.ForeignKey(User,blank=False,on_delete=models.CASCADE,related_name="created_user")

class Tasks(models.Model):
    title = models.CharField(blank=False, verbose_name="title")
    content = models.TextField(verbose_name="content")
    time = models.TimeField(default="08:00", verbose_name="time")
    category = models.ForeignKey(Categories,on_delete=models.SET_NULL,related_name="category", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="author")
    repeat_days = models.CharField(blank=True, verbose_name="r_days")
    status = models.BooleanField(blank=True, default=False)

