from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

# Create your views here.

class DjanguiHomeView(TemplateView):
    template_name = 'djangui_home.html'

    def get_context_data(self, **kwargs):
        ctx = super(DjanguiHomeView, self).get_context_data(**kwargs)
        ctx['djangui_apps'] = settings.DJANGUI_APPS
        return ctx