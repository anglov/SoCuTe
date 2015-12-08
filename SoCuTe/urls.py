from django.conf.urls import include, url
from django.contrib import admin
from socute_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'SoCuTe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^index/?$', views.index),
    url(r'^/?$', views.index),
]
