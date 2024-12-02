from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    title = models.CharField(max_length=75)
    outline = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_date']

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='project_images/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project images'
