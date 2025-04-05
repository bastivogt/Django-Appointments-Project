from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from appointments.forms import TagForm
from appointments.models import Tag

@login_required(login_url="sevo_user:sign_in")
def index(request):
    tags = Tag.objects.filter(user=request.user)
    print(tags)
    return render(request, "appointments/tags/index.html", {
        "title": "All Tags",
        "tags": tags
    })

@login_required(login_url="sevo_user:sign_in")
def new(request):
    if request.method == "POST":
        form = TagForm(request.POST, initial={"user": request.user})
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            messages.add_message(request, messages.SUCCESS, "Tag created!")
            return redirect("appointments:tags_index")
    else:
        form = TagForm(initial={"user": request.user})
    return render(request, "appointments/tags/new.html", {
        "title": "Create Tag",
        "form": form
    })

@login_required(login_url="sevo_user:sign_in")
def update(request, pk):
    tag = get_object_or_404(Tag, pk=pk, user=request.user)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Tag updated!")
            return redirect("appointments:tags_index")
    else:
        form = TagForm(instance=tag)
    return render(request, "appointments/tags/update.html", {
        "title": tag.title,
        "form": form
    })

@login_required(login_url="sevo_user:sign_in")
def show(request, pk):
    tag = get_object_or_404(Tag, pk=pk, user=request.user)
    appointments = tag.appointments.all()
    return render(request, "appointments/tags/show.html", {
        "title": f"{tag.title}",
        "tag": tag,
        "appointments": appointments
    })


@login_required(login_url="sevo_user:sign_in")
def delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk, user=request.user)
    if request.method == "POST":
        tag.delete()
        messages.add_message(request, messages.SUCCESS, "Tag deleted!")
        return redirect("appointments:tags_index")

    return render(request, "appointments/tags/confirm_delete.html", {
        "title": f"{tag.title}",
        "tag": tag
    })