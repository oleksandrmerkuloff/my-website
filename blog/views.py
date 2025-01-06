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

    session_key = f'viewed_post_{post.pk}'

    if not request.session.get(session_key, False):
        post.views += 1
        post.save()
        request.session[session_key] = True

    return render(request, 'blog/single_post.html',
                  {
                      'post': post,
                      'tags': tags,
                      'images': images
                    })
