from ..models import Marks,Student_data,Subject 
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse
from ..marks_form import MarksForm

class StudentDetail_mangementView(DetailView):
    def get(self, request, pk):
        student = get_object_or_404(Student_data, pk=pk)
        form = MarksForm()
        return render(request, 'marks_student_managment.html', {'student': student, 'form': form})

    def post(self, request, pk):
        student = get_object_or_404(Student_data, pk=pk)
        form = MarksForm(request.POST)
        
        if form.is_valid():
            sub= Subject.objects.get(subject_name=form.cleaned_data['subject'])
            cd = form.cleaned_data
            Marks.objects.create(
                student=student,
                subject=sub,
                marks_obtained=cd['marks_obtained'] 
            )
            return redirect(reverse('marks_student_management', kwargs={"pk": pk}))
        return render(request, 'marks_student_managment.html', {'student': student, 'form': form})


