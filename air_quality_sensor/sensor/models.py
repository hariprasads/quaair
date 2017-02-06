from django.db import models


# Create your models here.

class Route(models.Model):
    route_id = models.CharField(max_length=20, primary_key=True)

    zipcode = models.TextField(max_length=200)

    def __unicode__(self):
        return unicode(self.route_id)

    class Meta:
        app_label = 'sensor'


class Vehicle(models.Model):

    route = models.ForeignKey('Route')

    current_location = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        app_label = 'sensor'


class Sensors(models.Model):
    sensor_id = models.CharField(max_length=20, primary_key=True)

    TYPE = (
        ('GPS', 'GPS'),
        ('AirQuality', 'AirQuality'),
    )
    sensor_type = models.CharField(max_length=20, choices=TYPE)

    STATUS = (
        ('Active', 'Active'),
        ('Broken', 'Broken'),
        ('InActive', 'InActive'),
    )

    sensor_status = models.CharField(max_length=6, choices=STATUS)

    vehicle = models.ForeignKey('Vehicle')

    def __unicode__(self):
        return unicode(self.sensor_id)

    class Meta:
        app_label = 'sensor'

