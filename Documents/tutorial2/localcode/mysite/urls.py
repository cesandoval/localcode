from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

"""
urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)"""

urlpatterns = patterns('',
    url(r'^localcode/', include('localcode.urls', namespace="localcode")),
    url(r'^admin/', include(admin.site.urls)),
)