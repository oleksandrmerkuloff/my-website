from django.contrib import admin

from . import models


class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'outline', 'content')
    list_display = ['title', 'created_date', 'updated_date']
    list_display_links = ['title', ]


class ProjectImageAdmin(admin.ModelAdmin):
    fields = ('name', 'project', 'image')
    list_display = ['name', 'project', 'created_date']
    list_display_links = ['name']
    ordering = ['-created_date']


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.ProjectImage, ProjectImageAdmin)
