from django.shortcuts import render
from category_app.models import Category, Information


def home(request):

    return render(request, 'frontend/home.html', {'home': 'home'})


def about(request):

    return render(request, 'frontend/about.html', {'about': 'about'})


def contact(request):

    return render(request, 'frontend/contact_us.html', {'contact': 'contact'})


def tutorial(request):
    informations = Information.objects.all()

    context = {
        'informations': informations
    }
    return render(request, 'frontend/tutorial.html', context)


def choose(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'frontend/choose.html', context)


def proceed(request):

    return render(request, 'frontend/exam.html')
