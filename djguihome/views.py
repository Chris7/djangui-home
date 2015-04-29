from django.views.generic import TemplateView
from django.conf import settings

from djangui.models import DjanguiJob

class DjanguiHomeView(TemplateView):
    template_name = 'djangui_home.html'

    def get_context_data(self, **kwargs):
        task_id = self.request.GET.get('task_id')
        ctx = super(DjanguiHomeView, self).get_context_data(**kwargs)
        ctx['djangui_apps'] = getattr(settings, 'DJANGUI_SCRIPTS', {})
        if task_id:
            job = DjanguiJob.objects.get(celery_id=task_id)
            if job.user is None or (self.request.user.is_authenticated() and job.user == self.request.user):
                ctx['clone_job'] = {'task_id': task_id, 'url': job.get_resubmit_url()}
        return ctx