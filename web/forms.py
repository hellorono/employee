from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from web.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["emp_no","name","address","emp_start_date","emp_end_date","photo"]

        widgets={
            "emp_no":forms.TextInput(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "emp_start_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "emp_end_date":forms.DateInput(attrs={"class":"form-control", "type":"date", "format":"%Y-%m-%d"}),
            "photo":forms.FileInput(attrs={"class":"form-select"}),
            "emp_start_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "inputmode": "numeric"}),
            "emp_end_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "inputmode": "numeric"}),

            
        }

class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
