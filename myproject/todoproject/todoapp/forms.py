from django import forms
from .models import TASK


class TaskForm(forms.ModelForm):
    class Meta:
        model=TASK
        fields=['name','priority','date']