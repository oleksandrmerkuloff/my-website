from typing import Iterable
from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    short_desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    content = models.TextField()
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)


class Project(models.Model):
    title = models.CharField(max_length=150)
    short_desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    content = models.TextField()
    slug = models.SlugField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if not self.id:
            self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)
