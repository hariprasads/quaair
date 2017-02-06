from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vraManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'sensor/login.html'},
                           name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^', include('sensor.urls')),
    url(r'^sensor/', include('sensor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/djcelery', include(admin.site.urls)),
    # url(r'^node/', include('testbed.urls')),
    # url(r'^testbed/(?)/node/$', views.detail, name='detail'),
    url(r'^redactor/', include('redactor.urls')),
)