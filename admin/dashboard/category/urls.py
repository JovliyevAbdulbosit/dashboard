from django.urls import path 
from .views import categoryViews,categoryallViews,CategoryeditViews,detialViews,DeleteViews




urlpatterns=[path('form/', categoryViews, name='forms'),
path('list/', categoryallViews, name='list'),
path('<int:pk>/edit/', CategoryeditViews.as_view(), name='edit'),
path('<int:pk>/' , detialViews, name='detial'),
path('<int:pk>/delete/', DeleteViews.as_view(), name='delete')]