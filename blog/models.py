from django.utils.text import slugify
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=75, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', blank=True, null=False)
    outline = models.CharField(max_length=300)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_date']

    def __str__(self) -> str:
        return self.title


class PostImage(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='images')
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post Image'
        verbose_name_plural = 'Post images'
