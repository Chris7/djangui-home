from django.views.generic import TemplateView
from django.conf import settings

from djangui.backend import utils

class DjanguiHomeView(TemplateView):
    template_name = 'djangui_home.html'

    def get_context_data(self, **kwargs):
        task_id = self.request.GET.get('task_id')
        ctx = super(DjanguiHomeView, self).get_context_data(**kwargs)
        ctx['djangui_apps'] = settings.DJANGUI_APPS
        if task_id:
            from djguicore.models import DjanguiJob
            job = DjanguiJob.objects.get(djangui_celery_id=task_id)
            if job.djangui_user is None or (self.request.user.is_authenticated() and job.djangui_user == self.request.user):
                ctx['clone_job'] = {'task_id': task_id, 'url': utils.get_model_script_url(job.content_object)}
        return ctx