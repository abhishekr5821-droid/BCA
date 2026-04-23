from django.shortcuts import render, redirect, get_object_or_404
from .models import Timetable, Syllabus
from django.http import HttpResponse


# ✅ HOME
def home(request):
    return render(request, 'index.html')


# ✅ TIMETABLE
def timetable(request):
    data = Timetable.objects.all()
    return render(request, 'timetable.html', {'data': data})


# ✅ SYLLABUS VIEW
def syllabus_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        file = request.FILES.get("file")  # 👈 ADDED

        if title:
            Syllabus.objects.create(title=title, file=file)

        return redirect("syllabus")

    data = Syllabus.objects.all()
    return render(request, "syllabus.html", {"data": data})


# ✅ ADD SYLLABUS (UPDATED ONLY — NOT DUPLICATED)
def add_syllabus(request):
    if request.method == "POST":
        title = request.POST.get('title')
        file = request.FILES.get('file')  # 👈 ADDED

        if title:
            Syllabus.objects.create(title=title, file=file)

    return redirect('syllabus')


# ✅ DELETE
def delete_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id)
    syllabus.delete()
    return redirect('syllabus')


# ✅ UPDATE (kept as-is)
def update_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id)
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            syllabus.title = title
            syllabus.save()
            return redirect('syllabus')
    return render(request, 'update_syllabus.html', {'syllabus': syllabus})


# ✅ EDIT (kept as-is)
def edit_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, id=syllabus_id)
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            syllabus.title = title
            syllabus.save()
            return redirect('syllabus')
    return render(request, 'edit_syllabus.html', {'syllabus': syllabus})