from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from socute_app import views

urlpatterns = [
    url('^login/?$', views.log_in),
    url('^logout/?$', views.log_out),
    url('^register/?$', views.register),
    url('^posts/?$', views.posts),
    url('^add/?$', views.add),
    url('^post/?$', views.post),
    url('^index/?$', views.index),
    url(r'^/?$', views.index),
]
urlpatterns += staticfiles_urlpatterns()

