import os

from django.apps import AppConfig, apps
from django.conf import settings
from django.utils.module_loading import import_module
from django.core.urlresolvers import reverse_lazy

from djangui.backend import utils

class DjanguiHomeConfig(AppConfig):
    name = 'djguihome'
    verbose_name = 'Djangui home'

    def ready(self):
        djangui_apps = {}
        installed_apps = dict([(app, import_module(app)) for app in settings.INSTALLED_APPS])
        for app_name, app in installed_apps.iteritems():
            if getattr(app, 'DJANGUI_APP', False):
                djangui_apps[app_name] = {'url': reverse_lazy('{0}_home'.format(app_name)), 'app': app}
                config = apps.get_app_config(app_name)
                scripts = []
                for model in config.get_models():
                    if utils.is_djangui_model(model):
                        script_name = [i for i in model._meta.fields if i.name == 'djangui_script_name'][0].default
                        # the script name is normally a filepath, so fix this
                        script_name = os.path.splitext(os.path.split(script_name)[1])[0]
                        print model, script_name
                        # import pdb; pdb.set_trace();
                        scripts.append({
                            'description': model.djangui_model_description,
                            'url': utils.get_djangui_model_json_url(app_name, script_name),
                            'title': script_name
                        })
                djangui_apps[app_name].update({'scripts': scripts})
        settings.DJANGUI_APPS = djangui_apps