from django.shortcuts import render
from django.http import HttpResponse


def blog_page(request):
    return HttpResponse('<h1>Blog page</h1>')


def single_post(request, post_id):
    return HttpResponse(f'<h1>Post: {post_id}</h1>')
