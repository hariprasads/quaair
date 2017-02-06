from django.conf.urls import patterns, include, url
from analyser import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vraManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^analyser/', include('analyser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/djcelery', include(admin.site.urls)),
    # url(r'^node/', include('testbed.urls')),
    # url(r'^testbed/(?)/node/$', views.detail, name='detail'),
    url(r'^redactor/', include('redactor.urls')),
)
