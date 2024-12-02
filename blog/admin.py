from django.contrib import admin

from . import models


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'outline', 'content', 'tags')
    list_display = ['title', 'created_date', 'likes']
    list_display_links = ['title', ]
    list_filter = ['tags', ]


class PostImageAdmin(admin.ModelAdmin):
    fields = ('name', 'post', 'image')
    list_display = ['name', 'post', 'created_date']
    list_display_links = ['name']
    ordering = ['-created_date']


admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostImage, PostImageAdmin)
