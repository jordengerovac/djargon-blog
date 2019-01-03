from django.conf.urls import url
from . import views

app_name= 'entries'

urlpatterns = [
    url(r'^$', views.all_entries, name="all"),
    url(r'^create/$', views.entry_create, name="create"),
    url(r'^(?P<url>[\w-]+)/$', views.entry_detail, name="detail"),
]
