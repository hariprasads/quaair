__author__ = 'hanumesh'
from models import *


def new_route(route_id, zipcodes):

    route_instance = Route(route_id=route_id, zipcode=zipcodes)
    route_instance.save()


def new_vehicle(route_id):

    print route_id
    route_instance = Route.objects.get(route_id=route_id)
    zips = route_instance.zipcode

    current_location, temp = zips.split(",", 1)
    current_location.strip(" ")

    new_vehicle = route_instance.vehicle_set.create(current_location=current_location)


def new_sensor(vehicle_id, sensor_id, sensor_type, sensor_status):

    vehicle_instance = Vehicle.objects.get(id=vehicle_id)

    new_sensor = vehicle_instance.sensors_set.create(sensor_id=sensor_id, sensor_type=sensor_type, sensor_status=sensor_status)

