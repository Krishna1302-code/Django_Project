from django.db.models import Q
from django.shortcuts import render

from ..models import Faculty, Student_data, Subject


def Home_page(request):
    # print(request.META)
    count_total_faculty = Faculty.objects.count()
    total_students_enrolled = Student_data.objects.count()
    total_subject = Subject.objects.count()
    return render(
        request,
        "home_page.html",
        {
            "total_students_enrolled": total_students_enrolled,
            "count_total_faculty": count_total_faculty,
            "total_subject": total_subject,
        },
    )


def Total_student(request):
    query = request.GET.get("q")
    if query:
        student = Student_data.objects.filter(
            Q(student_name__iexact=query) | Q(last_name__iexact=query)
        )
        print(query)
    else:
        student = Student_data.objects.all()
    return render(request, "total-student.html", {"student": student})


# def Count_total_students(request):
#     print("hi")

#     print(list(Student_data.objects.all()))
#     return render(request,'home_page.html',{'total_students_enrolled':total_students_enrolled})
