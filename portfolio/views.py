from django.shortcuts import render, redirect
from django.core.paginator import Paginator
import markdown

from .models import Project


def portfolio_page(request):
    project_list = Project.objects.prefetch_related('images')
    paginator = Paginator(project_list, 4)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'portfolio/portfolio_page.html',
                  {
                      'page_object': page_object
                  })


def single_project(request, project_slug):
    project = Project.objects.get(slug=project_slug)
    project_content = markdown.markdown(project.content)
    images = project.images.all()[0]

    session_key = f'viewed_project_{project.pk}'

    if not request.session.get(session_key, False):
        project.views += 1
        project.save()
        request.session[session_key] = True

    return render(request, 'portfolio/single_project.html',
                  {
                      'project': project,
                      'project_content': project_content,
                      'images': images
                      })


def like_project(request, project_pk):
    project = Project.objects.get(pk=project_pk)

    session_key = f'liked_project_{project.pk}'

    if request.session.get(session_key, False):
        project.likes -= 1
        request.session[session_key] = False
    else:
        project.likes += 1
        request.session[session_key] = True

    project.save()

    return redirect('single-project-page', project_slug=project.slug)
