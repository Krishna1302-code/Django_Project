from django.urls import path

# from .views.student_views import student_list,Create_student,Update_student,Delete_student
from .views.detail_Marks import StudentDetailView
from .views.subject_views import SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView
from .views.marks_views import  MarksUpdateView, MarksDeleteView
from .views.detail_Marks import StudentDetailView
from .views.homepage_views import Home_page,Total_student
from .views.faculty_views import student_list,Create_student,Update_student,Delete_student,list_faculty
from .views.managment_views import student_list_managment,Create_student_managment,Update_student_managment,Delete_student_managment
from .views.marks_studentdetail_managment import StudentDetail_mangementView
from .views.marks_views_management import  MarksUpdate_management_View,MarksDelete_management_View
from .views.faculty_managment import faculty_list_managment,Create_faculty_managment,Update_faculty_managment,Delete_faculty_managment
from .views.auth_views import register,login_views
# login_views,logout_views,reset_password_views


urlpatterns = [

    
    path('',Home_page, name='home_page'),
    path('register/',register,name='registration'),
    path('login/',login_views,name='login'),
    # path('logout/',logout_views,name='logout')
    # path('reset_password/',registration_views,name='reset_password')
    path('total_students/',Total_student,name="total-student"),
    path('facultystudentlist/',student_list,name='student_list'),
    path('facultystudentadd/',Create_student, name='add_student'),
    path('facultystudentedit/<int:id>/',Update_student, name='edit_student'),
    path('facultystudentdelete/<int:id>/',Delete_student, name='delete_student'),
    path('student/<int:pk>/marks/', StudentDetailView.as_view(), name='student_marks'), 
    path('facultysubject/', SubjectListView.as_view(), name='subject_list'), 
    path('facultyaddsubject/', SubjectCreateView.as_view(), name='add_subject'),
    path('facultyeditsubject/<int:pk>/', SubjectUpdateView.as_view(), name='edit_subject'),
    path('facultydeletesubject/<int:pk>/', SubjectDeleteView.as_view(), name='delete_subject'),
    path('detail/<int:pk>/',StudentDetailView.as_view(),name ='detail_marks'),
    path('marks/edit/<int:pk>/', MarksUpdateView.as_view(), name='edit_marks'),
    path('marks/delete/<int:pk>/', MarksDeleteView.as_view(), name='delete_marks'),
    path('facultylist/',list_faculty, name='list_faculty'),
    path('studentlistmanagment/',student_list_managment,name='managment_list'),
    path('addmanagment/',Create_student_managment, name='add_student_management'),
    path('editmanagment/<int:id>/',Update_student_managment, name='managment_edit_student'),
    path('deletemanagment/<int:id>/',Delete_student_managment, name='managment_delete_student'),
    path('studentmarks/<int:pk>/marks/',StudentDetail_mangementView.as_view(), name='marks_student_management'),
    path('marks/editmanagement/<int:pk>/',  MarksUpdate_management_View.as_view(), name='edit_student_marks_management'),
    path('marks/deletemanagemnt/<int:pk>/', MarksDelete_management_View.as_view(), name='delete_studentmarks_management'),
    path('facultylistmanagment',faculty_list_managment,name='list_faculty_managment'),
    path('facultymanagmentadd/',Create_faculty_managment, name='add_faculty'),
    path('facultymanagmentupdate/<int:id>/',Update_faculty_managment, name='update_faculty_managment'), 
    path('deletefacultymanagment/<int:id>/',Delete_faculty_managment, name='delete_faculty_managment'),

    
]   

