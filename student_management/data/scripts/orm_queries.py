from data.models import Student_data, Subject
from django.db import connection


def run():
    Student_data.objects.create(
        student_name="Krishna",
        last_name="Joshi",
        email="krishna@gmail.com",
        contact_no="+919955556623",
        address="qqqwww",
        subject=Subject.objects.get(id=2),
    )
    print(connection.queries)

    # student =Student_data.objects.first()
    # print(student)


def create_subject():
    sub1 = Subject()
    sub2 = Subject()
    sub3 = Subject()

    sub1.subject_name = "English"
    sub1.save()
    sub2.subject_name = "Maths"
    sub2.save()
    sub3.subject_name = "Science"
    sub3.save()
