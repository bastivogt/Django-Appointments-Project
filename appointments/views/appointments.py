from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import HttpResponse

from appointments.models import Appointment
from appointments.forms import AppointmentForm




def index(request):
    apps = Appointment.objects.filter(user=request.user)
    return render(request, "appointments/index.html", {
        "title": "All Appointments",
        "appointments": apps,
        "has_expired": Appointment.has_expired(request.user)
    })



def new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST, initial={"user": request.user}, user=request.user)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user

            form_obj.save()
            form.save_m2m()

            messages.add_message(request, messages.SUCCESS, "Appointment created.")
            return redirect("appointments:index")
    else:
        form = AppointmentForm(initial={"user": request.user}, user=request.user)
    return render(request, "appointments/new.html", {
        "title": "Create Appointment",
        "form": form
    })

def delete_expired(request):
    if request.method == "POST":
        apps = Appointment.objects.filter(user=request.user)
        for app in apps:
            if app.is_expired():
                app.delete()
        messages.add_message(request, messages.SUCCESS, _("All expired Appointments deleted."))
        return redirect("appointments:index")
    
    return render(request, "appointments/confirm_delete_expired.html", {
        "title": _("Delete all expired Appointments")
    })


