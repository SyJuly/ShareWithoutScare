# shareWithoutScare/urls.py
from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from shareWithoutScare.models import Friend

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^friends/', ListView.as_view(queryset=Friend.objects.all().order_by("-name")[:25], template_name="friends.html"))
]