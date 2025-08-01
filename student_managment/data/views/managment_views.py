from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student_data,Faculty
    
# def list_managment(request):
#     return render (request,'managment_list.html')

# def View_all_student(request):
#     student = Student_data.objects.all()
#     return render(request,'student_list.html',{'student':student})

# def View_all_faculty(request):
#     faculty = Faculty.objects.all()
#     return render(request,'')



from django.shortcuts import render, redirect, get_object_or_404
from ..models import Student_data, Subject
from ..student_forms import StudentForm 

#List of the Student
def student_list_managment(request):
    student = Student_data.objects.all()
    return render(request,'managment_list.html',{'student':student})

#Create new student
def Create_student_managment(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = StudentForm(request.POST)# will take all the data which is filled-up by user to form also contains all the form input data as a dictionary-like object
        print(form.data)
        if form.is_valid():
            # sub = Subject.objects.get(subject_name= form.cleaned_data['subject'])
            Student_data.objects.create(  #create method is used to insert data to database it is used when valid return true
                student_name = form.cleaned_data['name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                contact_no = form.cleaned_data['contact_no'],
                address = form.cleaned_data['address'],
                gender = form.cleaned_data['gender'] ,
                

            )
            return redirect('managment_list')
        else:
            print("Data Invalid")
            print(form.errors)
    else:
        form=StudentForm()
        return render(request,'student_edit_managment.html',{'form':form})

#Updating the existing records
def Update_student_managment(request,id):
    student= get_object_or_404(Student_data,id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
          
           student.student_name = form.cleaned_data['name']
           student.last_name = form.cleaned_data['last_name']
           student.email = form.cleaned_data['email']
           print(str(form.cleaned_data['contact_no']))
           print(type(student.contact_no))
           student.contact_no= form.cleaned_data['contact_no']
           student.address = form.cleaned_data['address']
           student.gender = form.cleaned_data['gender'] 
        
           student.save()
           return redirect('managment_list')
        
    else:
     form = StudentForm(initial={
         'name': "Abc",
         'last_name':student.last_name,
         'email': student.email,
         'contact_no':student.contact_no,
         'address': student.address,
         'gender': student.gender,
    
         })
    return render (request,'student_edit_managment.html',{'form':form})

#Deleting the existing records
def Delete_student_managment(request,id):
    student= get_object_or_404(Student_data,id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('managment_list')
    return render(request,'student_delete_managment.html',{'student':student}) 
         
        







































# #list view for student_data
# class StudentListView(ListView):
#     model = Student_data
#     template_name = 'student_list.html'
#     context_object_name = 'student'
    
# #create view for student_data
# class StudentCreateView(CreateView):
#     model = Student_data
#     form_class = Input
#     template_name = 'edit_student.html'
#     success_url = reverse_lazy('student_list')

# #update view for student_data
# class StudentUpdateView(UpdateView):
#     model = Student_data
#     form_class = Input
#     template_name = 'edit_student.html'
#     success_url = reverse_lazy('student_list')

# #delete view for student_data
# class StudentDeleteView(DeleteView):
#     model = Student_data
#     template_name = 'delete_student.html'
#     success_url = reverse_lazy('student_list')

