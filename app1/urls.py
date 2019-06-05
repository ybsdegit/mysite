#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 0:08
# @Author  : Paulson
# @File    : urls.py
# @Software: PyCharm
# @define  : function

from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('index/', views.index),
    path('press_list/', views.press_list),
    path('add_press/', views.add_press),
    path('delete_press/', views.delete_press),
    path('edit_press/', views.edit_press),
    # ----------------- 书籍 -------------
    path('book_list/', views.book_list),
    path('add_book/', views.add_book),
    path('delete_book/', views.delete_book),
    path('edit_book/', views.edit_book),
    
    # ----------------- 作者 --------------
    path('author_list/', views.author_list),
    path('add_author/', views.add_author),
    path('delete_author/', views.delete_author),
    path('edit_author/', views.edit_author),
    path('upload/', views.upload),
]
