from django import forms
from phonenumber_field.formfields import PhoneNumberField


class StudentForm(forms.Form):

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

    student_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    contact_no = PhoneNumberField(region="IN")
    address = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    standard = forms.ChoiceField(choices=STANDARD_CHOICES)
