__author__ = 'hanumesh'

from django.core.management.base import BaseCommand
from sensor.models import *

class Command(BaseCommand):
    help = 'our help string comes here'

    def _create_sensor(self):
        # Insert all testbed into database

        r1 = Route(route_id='181', zipcode="95115,95116,95117")
        r1.save()

        r2 = Route(route_id='72', zipcode="95110,95111,95112")
        r2.save()

        route_instance1 = Route.objects.get(route_id="181")

        v1 = Vehicle(route = route_instance1, current_location = "95115")
        v1.save()

        
        v2 = Vehicle(route = route_instance1, current_location = "95116")
        v2.save()
        
        route_instance2 = Route.objects.get(route_id="72")
        
        v3 = Vehicle(route = route_instance1, current_location = "95110")
        v3.save()

        
        v4 = Vehicle(route = route_instance1, current_location = "95111")
        v4.save()
        
        
        vehicle_instance1 = Vehicle.objects.get(id="1")

        s1 = Sensors(sensor_id='1000', sensor_type='GPS', sensor_status="Active", vehicle=vehicle_instance1)
        s1.save() 
        
        s2 = Sensors(sensor_id='1001', sensor_type='AirQulaity', sensor_status="Active", vehicle=vehicle_instance1)
        s2.save()
        
        
        vehicle_instance1 = Vehicle.objects.get(id="2")

        s3 = Sensors(sensor_id='1002', sensor_type='GPS', sensor_status="Active", vehicle=vehicle_instance1)
        s3.save()
        
        s4 = Sensors(sensor_id='1003', sensor_type='AirQulaity', sensor_status="Active", vehicle=vehicle_instance1)
        s4.save()
        
        
        vehicle_instance1 = Vehicle.objects.get(id="3")

        s1 = Sensors(sensor_id='1004', sensor_type='GPS', sensor_status="Active", vehicle=vehicle_instance1)
        s1.save() 
        
        s2 = Sensors(sensor_id='1005', sensor_type='AirQulaity', sensor_status="Active", vehicle=vehicle_instance1)
        s2.save()
        
        
        vehicle_instance1 = Vehicle.objects.get(id="4")

        s1 = Sensors(sensor_id='1006', sensor_type='GPS', sensor_status="Active", vehicle=vehicle_instance1)
        s1.save() 
        
        s2 = Sensors(sensor_id='1007', sensor_type='AirQulaity', sensor_status="Active", vehicle=vehicle_instance1)
        s2.save()

    def handle(self, *args, **options):
        self._create_sensor()