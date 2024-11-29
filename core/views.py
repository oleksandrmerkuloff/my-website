from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>Home page</h1>')
