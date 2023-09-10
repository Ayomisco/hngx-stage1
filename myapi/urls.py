from django.urls import path
from myapi.views import MyApiView
from django.urls import re_path

urlpatterns = [
    re_path(r'^api$', MyApiView.as_view(), name='myapi')
]
