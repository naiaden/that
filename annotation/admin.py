from django.contrib import admin

from .models import Tweet
from annotation.models import Annotation_vl, Student, Annotation_eb

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Annotation_vl)
admin.site.register(Annotation_eb)
admin.site.register(Student)
