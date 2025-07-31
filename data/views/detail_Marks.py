from ..models import Marks,Student_data,Subject 
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse
from ..marks_form import MarksForm

class StudentDetailView(DetailView):
    def get(self, request, pk):
        student = get_object_or_404(Student_data, pk=pk)
        form = MarksForm()
        marks = Marks.objects.filter(student=student)# will get all marks for this student

        marks_obtained = sum(mark.marks_obtained for mark in marks)# Calculating total and percentage
        subject_count = marks.count()
        marks_per_subject = 100
        percentage = (marks_obtained / (subject_count * marks_per_subject)) * 100 if subject_count > 0 else 0

        return render(request, 'student_marks.html', {
            'student': student,
            'form': form,
            'marks': marks,
            'percentage': round(percentage, 2)
        })

    def post(self, request, pk):
        student = get_object_or_404(Student_data, pk=pk)
        form = MarksForm(request.POST)

        if form.is_valid():
            sub = Subject.objects.get(subject_name=form.cleaned_data['subject'])
            cd = form.cleaned_data
            Marks.objects.create(
                student=student,
                subject=sub,
                marks_obtained=cd['marks_obtained']
            )
            return redirect(reverse('student_marks', kwargs={"pk": pk}))

        












# from django.views import View
# from django.shortcuts import render, redirect, get_object_or_404
# from ..models import Student_data
# from ..marks_form import MarksForm

# class StudentDetailView(View):
#     def get(self, request, pk):
#         student = get_object_or_404(Student_data, pk=pk)
#         form = MarksForm()
#         return render(request, 'student_marks.html', {'student': student, 'form': form})

#     def post(self, request, pk):
#         student = get_object_or_404(Student_data, pk=pk)
#         form = MarksForm(request.POST)
#         if form.is_valid():
#             mark = form.save(commit=False)
#             mark.student = student
#             mark.save()
#             return redirect('student-marks', pk=pk)
#         return render(request, 'student_marks.html', {'student': student, 'form': form})
