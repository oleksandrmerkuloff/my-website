from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Home page")


def blog_page(request):
    return HttpResponse("Blog page")


def single_post(request, post_slug):
    return HttpResponse("Single post page")


def portfolio_page(request):
    return HttpResponse("Portfolio page")


def single_project(request, project_slug):
    return HttpResponse("Single project page")


def contacts_page(request):
    return HttpResponse("Contacts page")
