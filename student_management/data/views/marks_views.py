from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from ..marks_form import MarksForm
from ..models import Marks


class MarksUpdateView(UpdateView):
    model = Marks
    form_class = MarksForm
    template_name = "marks_edit.html"
    success_url = reverse_lazy("student_list")


class MarksDeleteView(DeleteView):
    model = Marks
    template_name = "marks_delete.html"
    success_url = reverse_lazy("student_list")


# def progress(request):
