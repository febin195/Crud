from django import forms
from crm.models import StudentModel,User


class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
    


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields="__all__"

class Loginform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        