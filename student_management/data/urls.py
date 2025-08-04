from django.urls import path

from .views.auth_views import (
    faculty_dashboard,
    login_views,
    register,
    student_dashboard,
)

# from .views.student_views import student_list,Create_student,Update_student,Delete_student
from .views.detail_Marks import StudentDetailView
from .views.faculty_management import (
    Create_faculty_management,
    Delete_faculty_management,
    Update_faculty_management,
    faculty_list_management,
)
from .views.faculty_views import (
    Create_student,
    Delete_student,
    Update_student,
    list_faculty,
    student_list,
)
from .views.homepage_views import Home_page, Total_student
from .views.management_views import (
    Create_student_management,
    Delete_student_management,
    Update_student_management,
    student_list_management,
)
from .views.marks_studentdetail_management import StudentDetail_mangementView
from .views.marks_views import MarksDeleteView, MarksUpdateView
from .views.marks_views_management import (
    MarksDelete_management_View,
    MarksUpdate_management_View,
)
from .views.subject_views import (
    SubjectCreateView,
    SubjectDeleteView,
    SubjectListView,
    SubjectUpdateView,
)

urlpatterns = [
    path("", Home_page, name="home_page"),
    path("register/", register, name="registration"),
    path("login/", login_views, name="login"),
    path("student/dashboard/", student_dashboard, name="student_dashboard"),
    path("faculty/dashboard/", faculty_dashboard, name="faculty_dashboard"),
    path("total_students/", Total_student, name="total-student"),
    path("facultystudentlist/", student_list, name="student_list"),
    path("facultystudentadd/", Create_student, name="add_student"),
    path("facultystudentedit/<int:id>/", Update_student, name="edit_student"),
    path("facultystudentdelete/<int:id>/", Delete_student, name="delete_student"),
    path("student/<int:pk>/marks/", StudentDetailView.as_view(), name="student_marks"),
    path("facultysubject/", SubjectListView.as_view(), name="subject_list"),
    path("facultyaddsubject/", SubjectCreateView.as_view(), name="add_subject"),
    path(
        "facultyeditsubject/<int:pk>/", SubjectUpdateView.as_view(), name="edit_subject"
    ),
    path(
        "facultydeletesubject/<int:pk>/",
        SubjectDeleteView.as_view(),
        name="delete_subject",
    ),
    path("detail/<int:pk>/", StudentDetailView.as_view(), name="detail_marks"),
    path("marks/edit/<int:pk>/", MarksUpdateView.as_view(), name="edit_marks"),
    path("marks/delete/<int:pk>/", MarksDeleteView.as_view(), name="delete_marks"),
    path("facultylist/", list_faculty, name="list_faculty"),
    path("studentlistmanagement/", student_list_management, name="management_list"),
    path("addmanagement/", Create_student_management, name="add_student_management"),
    path(
        "editmanagement/<int:id>/",
        Update_student_management,
        name="management_edit_student",
    ),
    path(
        "deletemanagement/<int:id>/",
        Delete_student_management,
        name="management_delete_student",
    ),
    path(
        "studentmarks/<int:pk>/marks/",
        StudentDetail_mangementView.as_view(),
        name="marks_student_management",
    ),
    path(
        "marks/editmanagement/<int:pk>/",
        MarksUpdate_management_View.as_view(),
        name="edit_student_marks_management",
    ),
    path(
        "marks/deletemanagemnt/<int:pk>/",
        MarksDelete_management_View.as_view(),
        name="delete_studentmarks_management",
    ),
    path(
        "facultylistmanagement", faculty_list_management, name="list_faculty_management"
    ),
    path("facultymanagementadd/", Create_faculty_management, name="add_faculty"),
    path(
        "facultymanagementupdate/<int:id>/",
        Update_faculty_management,
        name="update_faculty_management",
    ),
    path(
        "deletefacultymanagement/<int:id>/",
        Delete_faculty_management,
        name="delete_faculty_management",
    ),
]
