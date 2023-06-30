from django.forms import ModelForm
from django import forms
from .models import RegisterdUser

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisterdUser
        fields = '__all__'
        labels = {
            "name":"Username",
            "emailid":"Email Id",
            "phonenumber":"Phone Number",
            "password":"password"
        }