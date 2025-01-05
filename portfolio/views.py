from django.shortcuts import render

from .models import Project


def portfolio_page(request):
    projects = Project.objects.prefetch_related('images')
    return render(request, 'portfolio/portfolio_page.html',
                  {
                      'projects': projects
                  })


def single_project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    images = project.images.all()[0]
    return render(request, 'portfolio/single_project.html',
                  {
                      'project': project,
                      'images': images
                      })
