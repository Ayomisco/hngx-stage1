from django.urls import path
from myapi.views import MyApiView

urlpatterns = [
    path('api/', MyApiView.as_view(), name='myapi'),
]
