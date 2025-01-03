from django.urls import path

from . import views


urlpatterns = [
    path('', views.portfolio_page, name='portfolio'),
    path('<int:project_id>', views.single_project, name='single-project-page')
]
