from django.urls import path

from . import views


urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('<slug:post_slug>', views.single_post, name='single-post-page'),
    path('<int:post_pk>/like', views.like_post, name='like_post'),
]
