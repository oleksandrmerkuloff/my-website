from django.shortcuts import render
from django.http import HttpResponse

from .models import Project


def portfolio_page(request):
    projects = Project.objects.all()
    return HttpResponse('Project')
    # return render(request, 'portfolio/portfolio_page.html',
    #               {
    #                   'projects': projects
    #               })


def single_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    images = project.images.all()
    return render(request, 'portfolio/single_project.html',
                  {
                      'project': project,
                      'images': images
                      })
