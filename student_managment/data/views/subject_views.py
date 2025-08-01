from ..subject_form import SubjectForm 
from django.views.generic import ListView, UpdateView , CreateView, DeleteView
from django.urls import reverse_lazy
from ..models import Subject 

class SubjectListView(ListView):
    model = Subject
    template_name = 'subject_list.html'
    context_object_name= 'subject'
 
class SubjectCreateView(CreateView):
    model = Subject
    form_class =  SubjectForm 
    template_name = 'edit_subject.html'
    success_url = reverse_lazy('subject_list')

class SubjectUpdateView(UpdateView):
    model= Subject
    form_class =  SubjectForm 
    template_name = 'edit_subject.html'
    success_url= reverse_lazy('subject_list')

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'delete_subject.html'
    success_url= reverse_lazy('subject_list')