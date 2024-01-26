from django import forms
from .models import Task

class TasksCreate(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your description here'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }