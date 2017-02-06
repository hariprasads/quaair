from django.conf.urls import patterns, url, include
from analyser import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'air_quality', views.AirQualityViewSet)


urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'sensor_data', views.sensor_data, name='sensor_data'),
    url(r'^index', views.index, name="index"),
    url(r'^air_quality_data', views.air_quality_data, name="air_quality_data"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^about', views.about, name="about")
)
