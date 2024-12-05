from django.shortcuts import render


def home_page(request):
    return render(request, 'base.html')


def contacts(request):
    return render(request, 'contacts_page.html')
