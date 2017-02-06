from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
@login_required(login_url='/sensor/login/')
def index(request):
    """
    This view is to render the homepage of the dashboard.
    Args:
        request: url request by the user.
    """

    all_sensors = Sensors.objects.all()
    gps_sensors_count = 0
    air_quality_sensors_count = 0
    inactive_sensors_count = 0
    if all_sensors:
        for sensor in all_sensors:
            if sensor.sensor_type == 'GPS' and sensor.sensor_status == 'Active':
                gps_sensors_count += 1
            if sensor.sensor_type == 'AirQuality' and sensor.sensor_status == 'Active':
                air_quality_sensors_count += 1
            if sensor.sensor_status == 'InActive':
                inactive_sensors_count += 1

    vehicles_count = Vehicle.objects.count()

    routes_count = Route.objects.count()

    template = loader.get_template('sensor/admin281.html')
    context = RequestContext(request, {'gps_sensors_count': gps_sensors_count,
                                       'air_quality_sensors_count': air_quality_sensors_count,
                                       'inactive_sensors_count': inactive_sensors_count, 'vehicles_count': vehicles_count,
                                       'routes_count': routes_count})
    return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def routes(request):
    success = ""
    message = ""
    if 'success' in request.GET:
        success = request.GET['success']
    if 'msg' in request.GET:
        message = request.GET['msg']

    routes = Route.objects.all()

    template = loader.get_template('sensor/routes.html')
    context = RequestContext(request, {'routes': routes, 'success': success,
                                       'message': message})
    return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def sensors(request):
    success = ""
    message = ""
    if 'success' in request.GET:
        success = request.GET['success']
    if 'msg' in request.GET:
        message = request.GET['msg']

    sensors = Sensors.objects.all()

    template = loader.get_template('sensor/sensors.html')
    context = RequestContext(request, {'sensors': sensors, 'success': success,
                                       'message': message})
    return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def vehicles(request):
    success = ""
    message = ""
    if 'success' in request.GET:
        success = request.GET['success']
    if 'msg' in request.GET:
        message = request.GET['msg']

    vehicles = Vehicle.objects.all()

    template = loader.get_template('sensor/vehicles.html')
    context = RequestContext(request, {'vehicles': vehicles, 'success': success,
                                       'message': message})
    return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def add_route(request):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':

        # Get the details from POST request and save it to database.
        route_number = request.POST.get('route_number', '')
        zipcodes = request.POST.get('zipcodes', '')

        print route_number
        print zipcodes

        from sensor_manager import new_route
        new_route(route_number, zipcodes)
        success = True
        message = "Successfully added route " + route_number
        success = str(success)

        return HttpResponseRedirect(reverse('routes', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)

    # If a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'sensor/addroute.html')


@login_required(login_url='/sensor/login/')
def add_vehicle(request):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':

        # Get the details from POST request and save it to database.
        route_number = request.POST.get('route_number', '')

        from sensor_manager import new_vehicle
        new_vehicle(route_number)

        success = True
        message = "Successfully added vehicle for route" + route_number
        success = str(success)

        return HttpResponseRedirect(reverse('vehicles', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)

    # If a GET (or any other method) we'll create a blank form
    else:
        routes = Route.objects.all()
        template = loader.get_template('sensor/addvehicle.html')
        context = RequestContext(request, {'routes': routes})
        return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def add_sensor(request):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':

        # Get the details from POST request and save it to database.
        vehicle_number = request.POST.get('vehicle', '')
        sensor_id = request.POST.get('sensor_id', '')
        type = request.POST.get('type', '')
        status = request.POST.get('status', '')

        from sensor_manager import new_sensor
        sensor_exists = ''
        try:
            sensor_exists = Sensors.objects.get(sensor_id=sensor_id)
        except:
            pass
        if not sensor_exists:

            new_sensor(vehicle_number, sensor_id, type, status)
            success = True
            message = "Successfully added sensor " + sensor_id + " in vehicle " + vehicle_number
            success = str(success)
        else:
            success = False
            message = "Failed to add sensor " + sensor_id + " in vehicle " + vehicle_number + "Sensor ID already exists."
            success = str(success)

        return HttpResponseRedirect(reverse('sensors', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)

    # If a GET (or any other method) we'll create a blank form
    else:
        vehicles = Vehicle.objects.all()
        template = loader.get_template('sensor/addsensor.html')
        context = RequestContext(request, {'vehicles': vehicles})
        return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def remove_route(request):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':
        # Get the details from POST request and save it to database.
        route_id = request.POST.get('route_id', '')

        Route.objects.get(pk=route_id).delete()

        success = True
        message = "Successfully removed route " + route_id
        success = str(success)

        return HttpResponseRedirect(reverse('routes', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)


@login_required(login_url='/sensor/login/')
def remove_vehicle(request):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':
        # Get the details from POST request and save it to database.
        vehicle_id = request.POST.get('vehicle_id', '')

        vehicle = Vehicle.objects.get(pk=vehicle_id)
        vehicle.delete()

        success = True
        message = "Successfully removed vehicle " + vehicle_id
        success = str(success)

        return HttpResponseRedirect(reverse('vehicles', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)

@login_required(login_url='/sensor/login/')
def remove_sensor(request):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':
        # Get the details from POST request and save it to database.
        sensor_id = request.POST.get('sensor_id', '')

        sensor = Sensors.objects.get(pk=sensor_id)
        sensor.delete()

        success = True
        message = "Successfully removed sensor " + sensor_id
        success = str(success)

        return HttpResponseRedirect(reverse('sensors', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)

'''
@user_passes_test(lambda u: u.is_superuser)
def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if request.POST['admin'] == "1":
                User.objects.create_superuser(**form.cleaned_data)
            else:
                new_user = User.objects.create_user(**form.cleaned_data)
            # login(new_user, {'template_name': 'testbed/login.html'})
            # redirect, or however you want to get to the main view
            return redirect(index)
    else:
        form = UserForm()

    return render(request, 'testbed/registerUser.html', {'form': form})
'''


# Login
def userAuth(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next = request.POST['next']
                return HttpResponseRedirect(next)
    template = loader.get_template('sensor/admin281.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


@login_required(login_url='/sensor/login/')
def update_sensor(request, sensor_id):
    """
    A GET call to this view renders the dashboard homepage.
    A POST call to this view changes the status field of the testbed.
    Args:
        request: url request by the user.
        test_bed_id: id of the testbed whose status is to be changed.
    """

    if request.method == 'POST':

        # Get the details from POST request and save it to database.
        vehicle_number = request.POST.get('vehicle', '')
        sensor_id = request.POST.get('sensor_id', '')
        type = request.POST.get('type', '')
        status = request.POST.get('status', '')

        from sensor_manager import new_sensor

        this_sensor = Sensors.objects.get(sensor_id=sensor_id)
        this_vehicle = Vehicle.objects.get(id=vehicle_number)
        this_sensor.vehicle = this_vehicle
        this_sensor.sensor_status = status
        this_sensor.save()

        success = True
        message = "Successfully updated sensor " + sensor_id
        success = str(success)

        return HttpResponseRedirect(reverse('sensors', args=(), kwargs={}) + '?msg=' + message + '&success=' + success)

    # If a GET (or any other method) we'll create a blank form
    else:
        vehicles = Vehicle.objects.all()
        this_sensor = Sensors.objects.get(sensor_id=sensor_id)
        template = loader.get_template('sensor/updatesensor.html')
        context = RequestContext(request, {'vehicles': vehicles, 'this_sensor': this_sensor})
        return HttpResponse(template.render(context))