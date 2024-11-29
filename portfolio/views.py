from django.shortcuts import render
from django.http import HttpResponse


def portfolio_page(request):
    return HttpResponse('<h1>Portfolio page</h1>')


def single_project(request, project_id):
    return HttpResponse(f'<h1>Project: {project_id}</h1>')
