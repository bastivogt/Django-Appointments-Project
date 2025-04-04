from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from appointments.forms import TagForm
from appointments.models import Tag


def index(request):
    tags = Tag.objects.filter(user=request.user)
    print(tags)
    return render(request, "appointments/tags/index.html", {
        "title": "All Tags",
        "tags": tags
    })


def new(request):
    if request.method == "POST":
        form = TagForm(request.POST, initial={"user": request.user})
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            messages.add_message(request, messages.SUCCESS, "Tag created.")
            return redirect("appointments:tags_index")
    else:
        form = TagForm(initial={"user": request.user})
    return render(request, "appointments/tags/new.html", {
        "title": "Create Tag",
        "form": form
    })


def update(request, pk):
    tag = get_object_or_404(Tag, pk=pk, user=request.user)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Tag updated.")
            return redirect("appointments:tags_index")
    else:
        form = TagForm(instance=tag)
    return render(request, "appointments/tags/update.html", {
        "title": tag.title,
        "form": form
    })


def show(request, pk):
    tag = get_object_or_404(Tag, pk=pk, user=request.user)
    appointments = tag.appointments.all()
    return render(request, "appointments/tags/show.html", {
        "title": f"#{tag.pk} - {tag.title}",
        "tag": tag,
        "appointments": appointments
    })



def delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk, user=request.user)
    if request.method == "POST":
        tag.delete()
        messages.add_message(request, messages.SUCCESS, "Tag deleted.")
        return redirect("appointments:tags_index")

    return render(request, "appointments/tags/confirm_delete.html", {
        "title": f"#{tag.pk} - {tag.title}",
        "tag": tag
    })