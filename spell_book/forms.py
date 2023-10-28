from spell_book.models import Scroll
from django import forms
from django.forms import ModelForm

class CreatingScrolls(ModelForm):
    class Meta:
        model = Scroll
        fields = ["title", "image_url", "content"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Title',
                                                'required': 'required'}),
            'image_url': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Image URL',
                                                'required': 'required'}),
            'content': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Content',
                                                'required': 'required'}),
        }