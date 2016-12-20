from django.shortcuts import render, redirect
from .models import User, Appointments
from django.contrib import messages
import datetime as dt


# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def register(request):
    viewsResponse = User.objects.add_user(request.POST)
    if viewsResponse['isRegistered']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('users:appointments')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('users:index')
def login(request):
    viewsResponse = User.objects.login_user(request.POST)
    if viewsResponse['isLoggedIn']:
        request.session['user_id'] = viewsResponse['user'].id
        request.session['user_fname'] = viewsResponse['user'].first_name
        return redirect('users:appointments')
    else:
        for error in viewsResponse['errors']:
            messages.error(request, error)
        return redirect('users:index')
def appointments(request):
    context = {
        'appointments': Appointments.objects.all(),
    }
    request.session['today'] = dt.datetime.today().strftime("%m/%d/%Y")
    if 'user_fname' not in request.session:
        messages.error(request, "You must be logged in to view your appointments")
        return redirect('users:index')

    return render(request, 'main/appointments.html', context)
def logout(request):
    request.session.clear()
    return redirect('users:index')
def delete(request, appointments_id):
    Appointments.objects.get(id = appointments_id).delete()
    return redirect('users:appointments')
def edit(request, appointments_id):
    context = {
        'appointment': Appointments.objects.get(id=appointments_id),
    }
    request.session['tasks'] = Appointments.objects.get(id=appointments_id).tasks
    request.session['date'] = Appointments.objects.get(id=appointments_id).appointDay
    request.session['time'] = Appointments.objects.get(id=appointments_id).appointTime
    Appointments.objects.get(id = appointments_id).delete()
    return render(request, 'main/edit.html')
def addAppointment(request):
    appointmentResponse = Appointments.objects.add_appointment(request.POST)
    if appointmentResponse['isValid']:
        return redirect('users:appointments')
    else:
        for error in appointmentResponse['errors']:
            messages.error(request, error)
            return redirect('users:appointments')
def editAppointment(request):

    appointmentResponse = Appointments.objects.edit_appointment(request.POST)
    if appointmentResponse['isValid']:
        return redirect('users:appointments')
    else:
        for error in appointmentResponse['errors']:
            messages.error(request, error)
            return render(request, 'main/edit.html')
