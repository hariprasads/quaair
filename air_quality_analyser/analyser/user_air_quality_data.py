__author__ = 'hanumesh'

from models import UserAirQualityData, AirQuality
from django.db.models import Q
from celery import task, group, Celery

app = Celery('portal')


def run_update_content():

    """
    """
    calculate_user_air_quality_data.apply_async(args=[], queue='periodical')


@app.task()
def calculate_user_air_quality_data():

    zipcodes = AirQuality.objects.values('location_zipcode').distinct()
    print zipcodes
    for zipcode in zipcodes:
        user_data = UserAirQualityData.objects.filter(location_zipcode=zipcode['location_zipcode'])
        if user_data:
            user_data.delete()

        zips_sensor_data = AirQuality.objects.filter(location_zipcode=zipcode['location_zipcode'])
        total = 0
        size = len(zips_sensor_data)
        for zip_sensor_data in zips_sensor_data:
            print zip_sensor_data.location_zipcode
            total += int(zip_sensor_data.air_quality)

        air_quality_data = str(int(total/size))

        save_data = UserAirQualityData(location_zipcode=zipcode['location_zipcode'], air_quality=air_quality_data)
        save_data.save()
