from django.urls import path 
from .views import *



urlpatterns=[path('ret_form/', retseptViews , name='retsept'),

path('ret_list/', retseptallViews, name='ret_list'),
path('<int:pk>/ret_edit/', RetsepteditViews.as_view(), name='ret_edit'),
path('<int:pk>/ret/' , retseptdetialViews, name='ret_detial'),
path('<int:pk>/ret_delete/', RetseptDeleteViews.as_view(), name='ret_delete')]

