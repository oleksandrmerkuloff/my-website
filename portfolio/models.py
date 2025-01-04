from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    title = models.CharField(max_length=75)
    outline = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(default='', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_date']

    def __str__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(upload_to='project_images/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project images'
