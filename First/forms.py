from django import forms
from django.forms import fields
from .models import Flight
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import  DateTimeField, DateInput
from bootstrap_datepicker_plus.widgets import DatePickerInput

class AddSchaduleForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields =('Flight_Origin','Flight_Distination','Flight_Airline','Flight_Nomber','Flight_Date','Flight_Time','schadule_Date','schadule_Time')