from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from .models import *
from django.forms import ModelForm

class StaffRegistrationForm(UserCreationForm):
    fname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    )) 

    lname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))     

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'EMP Number'
        }
    )) 
    
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))     

    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class StudentRegistrationForm(UserCreationForm):
    fname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    )) 

    lname = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    )) 

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'REG Number'
        }
    )) 
    
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))     

    class Meta:
        model = User
        fields = ('username', 'email', 'is_admin', 'is_staff', 'is_student')        

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    )) 
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': ''
        }
    ))           



class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = "__all__" 

class AcadYearForm(ModelForm):
    class Meta:
        model = AcadYear
        fields = "__all__" 


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__" 