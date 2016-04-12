from . import views
from django.conf.urls import url

app_name = 'annotate'

urlpatterns = [
    # /annotate/
    url(r'^$', views.index, name='index'),
    
    # /annotate/<student_id>/
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    
    # /annotate/<student_id>/addannotation/
    url(r'^(?P<student_id>[0-9]+)/addannotation$', views.addannotation, name='addannotation'),

    # /annotate/<student_id>/annotations/
    url(r'^(?P<student_id>[0-9]+)/annotations$', views.annotations, name='annotations')
]