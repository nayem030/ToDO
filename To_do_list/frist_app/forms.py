from django import forms
from . import models
class DoToForm(forms.ModelForm):
    class Meta:
        model=models.ToDoModel
        fields='__all__'
        