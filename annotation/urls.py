from . import views
from django.conf.urls import url

app_name = 'annotation'

urlpatterns = [
    # /annotation/
    url(r'^$', views.index, name='index'),
    
    # /annotation/<tweet_id>/
    url(r'^(?P<tweet_id>[0-9]+)/$', views.detail, name='detail'),
]