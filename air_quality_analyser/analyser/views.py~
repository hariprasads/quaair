from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import RequestContext, loader
from models import AirQuality, UserAirQualityData
from rest_framework import viewsets
from serializers import AirQualitySerializer


# Create your views here.
def index(request):
    """
    This view is to render the homepage of the dashboard.
    Args:
        request: url request by the user.
    """
    locations = UserAirQualityData.objects.all()

    template = loader.get_template('analyser/index.html')
    context = RequestContext(request, {'locations': locations})
    return HttpResponse(template.render(context))


def air_quality_data(request):

    if request.method == 'POST':

        location = request.POST.get('location', '')

        user_data = UserAirQualityData.objects.get(location_zipcode=location)

        chart_data = int(user_data.air_quality)

        print chart_data

        locations = UserAirQualityData.objects.all()

        template = loader.get_template('analyser/index.html')
        context = RequestContext(request, {'locations': locations, 'chart_data': chart_data})
        return HttpResponse(template.render(context))

def about(request):
    """
    This view is to render the homepage of the dashboard.
    Args:
        request: url request by the user.
    """

    template = loader.get_template('analyser/about.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


class AirQualityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AirQuality.objects.all().order_by('-date_joined')
    serializer_class = AirQualitySerializer


