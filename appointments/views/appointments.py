from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from appointments.models import Appointment
from appointments.forms import AppointmentForm



@login_required(login_url="sevo_user:sign_in")
def index(request):
    apps = Appointment.objects.filter(user=request.user)
    return render(request, "appointments/index.html", {
        "title": _("All Appointments"),
        "appointments": apps,
        "has_expired": Appointment.has_expired(request.user)
    })


@login_required(login_url="sevo_user:sign_in")
def new(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST, initial={"user": request.user}, user=request.user)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user

            form_obj.save()
            form.save_m2m()

            messages.add_message(request, messages.SUCCESS, "Appointment created!")
            return redirect("appointments:index")
    else:
        form = AppointmentForm(initial={"user": request.user}, user=request.user)
    return render(request, "appointments/new.html", {
        "title": _("Create Appointment"),
        "form": form
    })

@login_required(login_url="sevo_user:sign_in")
def delete_expired(request):
    if request.method == "POST":
        apps = Appointment.objects.filter(user=request.user)
        for app in apps:
            if app.is_expired():
                app.delete()
        messages.add_message(request, messages.SUCCESS, _("All expired Appointments deleted!"))
        return redirect("appointments:index")
    
    return render(request, "appointments/confirm_delete_expired.html", {
        "title": _("Delete all expired Appointments")
    })

@login_required(login_url="sevo_user:sign_in")
def update(request, pk):
    model = get_object_or_404(Appointment, user=request.user, pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=model, user=request.user)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            form.save_m2m()
            messages.add_message(request, messages.SUCCESS, "Appointment updated!")
            return redirect("appointments:index")
    else:
        form = AppointmentForm(instance=model, user=request.user)
    return render(request, "appointments/update.html", {
        "title": f"{model.title}",
        "form": form
    })


@login_required(login_url="sevo_user:sign_in")
def show(request, pk):
    model = get_object_or_404(Appointment, pk=pk, user=request.user)
    return render(request, "appointments/show.html", {
        "title": model.title,
        "appointment": model
    })


@login_required(login_url="sevo_user:sign_in")
def delete(request, pk):
    model = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == "POST":
        model.delete()
        messages.add_message(request, messages.SUCCESS, _("Apointment deleted!"))
        return redirect("appointments:index")

    return render(request, "appointments/confirm_delete.html", {
        "title": model.title,
        "appointment": model
    })


