from django import forms
from django.forms import fields
from .models import Flight

class AddSchaduleForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields =('Flight_Origin','Flight_Distination','Flight_Airline','Flight_Nomber','Flight_Date','is_valid','schadule_Date','schadule_Time',)
        
