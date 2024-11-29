from django.urls import path

from . import views


urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('<int:post_id>', views.single_post)
]
