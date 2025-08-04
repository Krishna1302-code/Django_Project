from django import forms

from .models import Marks


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = "marks_obtained", "subject", "standard"
