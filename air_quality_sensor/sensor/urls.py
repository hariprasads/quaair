from django.conf.urls import patterns, url
from sensor import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^add_route/', views.add_route, name='add_route'),
    url(r'^remove_route/', views.remove_route, name='remove_route'),
    url(r'^routes/', views.routes, name='routes'),
    url(r'^add_vehicle/', views.add_vehicle, name='add_vehicle'),
    url(r'^remove_vehicle/', views.remove_vehicle, name='remove_vehicle'),
    url(r'^vehicles/', views.vehicles, name='vehicles'),
    url(r'^add_sensor/', views.add_sensor, name='add_sensor'),
    url(r'^remove_sensor/', views.remove_sensor, name='remove_sensor'),
    url(r'^update_sensor/(?P<sensor_id>\d+)/', views.update_sensor, name='update_sensor'),
    url(r'^update_sensor/', views.update_sensor, name='update_sensor'),
    url(r'^sensors/', views.sensors, name='sensors'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'sensor/login.html'},
                           name='login'),

)
