from django.shortcuts import render

from .models import Post


def blog_page(request):
    posts = Post.objects.prefetch_related('images')
    return render(request, 'blog/blog_page.html',
                  {
                      'posts': posts
                  })


def single_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    tags = post.tags.all()
    images = post.images.all()[0]
    return render(request, 'blog/single_post.html',
                  {
                      'post': post,
                      'tags': tags,
                      'images': images
                    })
