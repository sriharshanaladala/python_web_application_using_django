from django.contrib import admin

# Register your models here.
from . models import Project, Review, tag

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(tag)
