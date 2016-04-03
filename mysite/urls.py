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
    url(r'^wx_index/',wx_index),
    url(r'^wx_detail/',wx_detail),
    url(r'^wx_search/',wx_search),
    url(r'^wx_search_ad/',wx_search_ad),
    url(r'^wx_mv_list/',wx_mv_list),
)
