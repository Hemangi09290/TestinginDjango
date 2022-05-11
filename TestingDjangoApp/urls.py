from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
url(r'^$', views.savedata),
path('/del/', views.deledata),
]