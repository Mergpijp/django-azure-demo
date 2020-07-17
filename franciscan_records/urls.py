# franciscan_records/urls.py
from django.conf.urls import url
from django.urls import path
from franciscan_records import views


urlpatterns = [
    path('', views.index, name='index'),
]