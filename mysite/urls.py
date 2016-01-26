from django.conf.urls import patterns, include, url
from django.contrib import admin
from movie.views.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # index loading
    url(r'^index/', index),
    url(r'^detail/', detail),
    url(r'^list/', list),
)
