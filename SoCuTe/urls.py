from django.conf.urls import include, url
from django.contrib import admin
from socute_app import views

urlpatterns = [
    url('^login/?$', views.log_in),
    url('^logout/?$', views.log_out),
    url('^register/?$', views.register),
    url('^posts/?$', views.posts),
    url('^add/?$', views.add),
    url('^post/?$', views.index),
    url('^index/?$', views.index),
    url(r'^/?$', views.index),
]
