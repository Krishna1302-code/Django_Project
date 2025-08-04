from django.shortcuts import get_object_or_404, redirect, render

from ..faculty_form import FacultyForm
from ..models import Faculty


def faculty_list_management(request):
    faculty = Faculty.objects.all()
    return render(request, "list_faculty_management.html", {"faculty": faculty})


# def Count_total_faculty(request):
#     count_total_faculty = Faculty.objects.count()
#     return render(request,'home_page.html',{'count_total_faculty':count_total_faculty})


def Create_faculty_management(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            faculty_name = form.cleaned_data["faculty_name"]
            subjects = form.cleaned_data["subject"]

            faculty = Faculty.objects.create(faculty_name=faculty_name)
            faculty.subject.set(subjects)
            return redirect("list_faculty_management")
    else:
        form = FacultyForm()
    return render(request, "edit_faculty_management.html", {"form": form})


def Update_faculty_management(request, id):
    faculty = get_object_or_404(Faculty, id=id)

    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            faculty.faculty_name = form.cleaned_data["faculty_name"]
            faculty.subject.set(form.cleaned_data["subject"])
            faculty.save()
            return redirect("list_faculty_management")
    else:
        form = FacultyForm(
            initial={
                "faculty_name": faculty.faculty_name,
                "subject": faculty.subject.all(),
            }
        )

    return render(request, "edit_faculty_management.html", {"form": form})


def Delete_faculty_management(request, id):
    faculty = get_object_or_404(Faculty, id=id)
    if request.method == "POST":
        faculty.delete()
        return redirect("list_faculty_management")
    return render(request, "delete_faculty_management.html", {"faculty": faculty})
