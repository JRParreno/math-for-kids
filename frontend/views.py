from django.shortcuts import render


def home(request):

    return render(request, 'frontend/home.html', {'home': 'home'})


def about(request):

    return render(request, 'frontend/about.html', {'about': 'about'})


def contact(request):

    return render(request, 'frontend/contact_us.html', {'contact': 'contact'})


def choose(request):

    return render(request, 'frontend/choose.html')


def tutorial(request):

    return render(request, 'frontend/tutorial.html')
