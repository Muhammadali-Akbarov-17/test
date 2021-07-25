from django.db import models
from django.forms import ModelForm, fields
from .models import Todoapp


class TodoForm(ModelForm):
    class Meta:
        model = Todoapp
        fields = ['title','description','is_done']

