from django.db import models
from django.shortcuts import render
from django.urls.base import reverse
from .models import Todoapp
from django.views.generic import  ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


class TodoappListView(ListView):
    model = Todoapp
    template_name = 'todoapp_list.html'

class TodoappDetailView(DetailView):
    model = Todoapp
    template_name = 'todoapp_detail.html'


class TodoappCreateView(CreateView):
    model = Todoapp
    template_name = 'todoapp_new.html'
    fields = ['title','description','is_done']

class TodoappUpdateView(UpdateView):
    model = Todoapp
    template_name = 'todoapp_edit.html'
    fields = ['title','description','is_done']

class TodoappDeleteView(DeleteView):
    model = Todoapp
    template_name = 'todoapp_delete.html'
    success_url = reverse_lazy('todo_list')
