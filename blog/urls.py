from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/<slug:post_slug>', views.single_post, name='single-post'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('portfolio/<slug:project_slug>', views.single_project,
         name='single-project'),
    path('contacts/', views.contacts_page, name='contacts'),
]
