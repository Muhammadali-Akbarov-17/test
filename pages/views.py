from django.shortcuts import render
from django.views.generic import ListView,TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
