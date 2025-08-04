from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student_data(models.Model):
    GENDER_CHOICES = [
        ("F", "FEMALE"),
        ("M", "MALE"),
        ("O", "OTHERS"),
    ]

    STANDARD_CHOICES = [
        ("1", "1st"),
        ("2", "2nd"),
        ("3", "3rd"),
        ("4", "4th"),
        ("5", "5th"),
        ("6", "6th"),
        ("7", "7th"),
        ("8", "8th"),
        ("9", "9th"),
        ("10", "10th"),
        ("11", "11th"),
        ("12", "12th"),
    ]

    from django.conf import settings

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    student_name = models.CharField(
        max_length=100,
        blank=False,
    )
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    contact_no = PhoneNumberField(unique=True, blank=False)
    address = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    standard = models.CharField(
        max_length=5, choices=STANDARD_CHOICES, null=True, blank=True
    )

    def __str__(self):
        return f"{self.student_name} {self.last_name}"


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subject_name


class Faculty(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    faculty_name = models.CharField(max_length=100, blank=False)
    subject = models.ManyToManyField(Subject, related_name="faculty")

    def __str__(self):
        return self.faculty_name


class Marks(models.Model):
    marks_obtained = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student_data, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.marks_obtained)


from django.contrib.auth.models import AbstractUser
from django.db import models


class Custom_User(AbstractUser):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("faculty", "Faculty"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
