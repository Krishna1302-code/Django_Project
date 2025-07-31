from django.contrib import admin
from .models import Student_data,Subject,Faculty,Marks

class StudentAdmin(admin.ModelAdmin):
    list_display= ['student_name', 'last_name','email','contact_no','address','gender']

admin.site.register(Student_data,StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display= ['subject_name']

admin.site.register(Subject,SubjectAdmin)

class FacultyAdmin(admin.ModelAdmin):
    list_display= ['faculty_name']

admin.site.register(Faculty,FacultyAdmin)

class MarksAdmin(admin.ModelAdmin):
    list_display= ['marks_obtained','student','subject']

admin.site.register(Marks,MarksAdmin)
