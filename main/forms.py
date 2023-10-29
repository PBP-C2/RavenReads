from django.forms import ModelForm
from main.models import Person, MainThread, Thread
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class PersonForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['tipe'].widget.attrs['class'] = 'form-control tipe'
        self.fields['tipe'].widget.attrs['placeholder'] = 'Tipe'
        self.fields['tipe'].widget.attrs['readonly'] = True
        self.fields['gender'].widget.attrs['class'] = 'form-control'

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
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]