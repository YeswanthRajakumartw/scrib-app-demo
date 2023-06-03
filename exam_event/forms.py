from django import forms

from .models import Exam
from tempus_dominus.widgets import DatePicker


class ExamForm(forms.ModelForm):
    date = forms.DateField(widget=DatePicker())

    class Meta:
        model = Exam
        fields = ('name', 'date', 'tickets_available')
