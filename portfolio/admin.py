from django.contrib import admin
from .models import Project, Comment, Like

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Like)