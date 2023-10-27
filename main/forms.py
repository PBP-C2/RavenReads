from django.forms import ModelForm
from main.models import Person, MainThread, Thread, QuizPoint
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class PersonForm(ModelForm):
    GENDER = (
        ('Male', 'male'),
        ('Female', 'female'),
    )

    gender = forms.ChoiceField(choices=GENDER)
    class Meta:
        model = Person
        fields = ["name", "email", "tipe", "gender"]
        

class MainThreadForm(ModelForm):
    class Meta:
        model = MainThread
        fields = ["title", "content"]

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ["content"]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Password',
                                                'required': 'required'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 
                                                    'placeholder': 'Password',
                                                    'required': 'required'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }