from django.template.defaultfilters import slugify
from django.db import models
from typing import Iterable


class Tag(models.Model):
    name = models.CharField(max_length=75, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    outline = models.CharField(max_length=300)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_date']

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post images'
