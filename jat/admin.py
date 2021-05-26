from django.contrib import admin

from jat.models import Repository, Comment, Introduction

admin.site.register(Repository)
admin.site.register(Introduction)
admin.site.register(Comment)