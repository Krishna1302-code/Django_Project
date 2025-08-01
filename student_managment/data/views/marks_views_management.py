from .. models  import Marks
from .. marks_form import MarksForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView


class MarksUpdate_management_View(UpdateView):
    model = Marks
    form_class = MarksForm
    template_name = 'edit_student_marks_managment.html'
    success_url= reverse_lazy('managment_list')

class MarksDelete_management_View(DeleteView):
    model = Marks
    template_name= 'delete_studentmarks_management.html'
    success_url=reverse_lazy('managment_list')
   
    