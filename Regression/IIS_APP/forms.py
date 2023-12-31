from django.forms import ModelForm
from django import forms
from .models import RegisterdUser,CreateTestsuite

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


class CreateTestsuiteForm(ModelForm):
    class Meta:
        model = CreateTestsuite
        fields = '__all__'
        labels = {
            "jobname": "jobname",
            "emailid": "emailid",
            "Testsuite": "Testsuite",
            "envirionment": "envirionment"
        }
class CSVUploadForm(forms.Form):
        csv_file = forms.FileField()