from django.shortcuts import render


def home(request):
    """ return home page """
    return render(request, 'core/home.html')


def about(request):
    """" return about page """
    return render(request, 'core/about.html')