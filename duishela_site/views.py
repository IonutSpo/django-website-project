from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'base.html'


class MainPage(TemplateView):
    template_name = 'main.html'