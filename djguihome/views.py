from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.utils.module_loading import import_module
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class DjanguiHomeView(TemplateView):
    template_name = 'djangui_home.html'

    def get_context_data(self, **kwargs):
        ctx = super(DjanguiHomeView, self).get_context_data(**kwargs)
        apps = dict([(app, import_module(app)) for app in settings.INSTALLED_APPS])
        # TODO: Move this to app config stage to do it only once
        djangui_apps = {}
        for app_name, app in apps.iteritems():
            if getattr(app, 'DJANGUI_APP', False):
                djangui_apps[app_name] = {'url': reverse_lazy('{0}_home'.format(app_name)), 'app': app}
        ctx['djangui_apps'] = djangui_apps
        return ctx