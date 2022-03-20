from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('main'))
        return super().get(request, *args, **kwargs)


class MainPage(TemplateView):
    template_name = 'main.html'
