from django.urls import path, include



urlpatterns=[path('adminchik/', include("dashboard.category.urls")),
path('adminchik/', include('dashboard.retsept.urls'))]
