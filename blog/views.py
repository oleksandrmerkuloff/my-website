from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Post


def blog_page(request):
    post_list = Post.objects.prefetch_related('images')
    paginator = Paginator(post_list, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'blog/blog_page.html',
                  {
                      'page_object': page_object
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


def like_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    session_key = f'liked_post_{post.pk}'

    if request.session.get(session_key, False):
        post.likes -= 1
        request.session[session_key] = False
    else:
        post.likes += 1
        request.session[session_key] = True

    post.save()

    return redirect('single-post-page', post_slug=post.slug)
