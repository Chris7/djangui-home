from django.conf.urls import include, url
from .views import DjanguiHomeView

urlpatterns = [
    url(r'^$', DjanguiHomeView.as_view(), name='djangui_home'),
]