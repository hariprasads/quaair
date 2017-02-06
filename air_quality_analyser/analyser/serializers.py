__author__ = 'hanumesh'

#from django.contrib.auth.models import User, Group
from models import AirQuality
from rest_framework import serializers

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
'''

class AirQualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AirQuality
        fields = ('vehicle_id', 'data_received_time', 'air_quality', 'location_zipcode')
