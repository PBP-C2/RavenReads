from django.forms import ModelForm
from main.models import Person, MainThread, Thread

class PersonForm(ModelForm):
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