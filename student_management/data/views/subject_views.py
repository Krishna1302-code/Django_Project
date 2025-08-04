from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..models import Subject
from ..subject_form import SubjectForm


class SubjectListView(ListView):
    model = Subject
    template_name = "subject_list.html"
    context_object_name = "subject"


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "edit_subject.html"
    success_url = reverse_lazy("subject_list")


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "edit_subject.html"
    success_url = reverse_lazy("subject_list")


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "delete_subject.html"
    success_url = reverse_lazy("subject_list")
