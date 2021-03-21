from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404
from category_app.models import Category, Information
import random


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


def proceed(request, operation):
    operator = {'multiplication': 'x', 'division': '/',
                'addition': '+', 'subtraction': '-'}
    colors = {'primary': 'text-white', 'success':
              'text-white', 'danger': 'text-white', 'warning': 'text-dark', 'info': 'text-dark', 'dark': 'text-white'}

    def random_nth_digit(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return random.randint(range_start, range_end)

    if request.method == 'POST':
        setting = request.POST.getlist('examSetting')
        range_exam = int(setting[0])
        first_len = int(setting[1])
        second_len = int(setting[2])
        questions = []

        for i in range(range_exam):
            inner_dict = dict()
            first_val = 0
            second_val = random_nth_digit(second_len)
            while first_val <= second_val:
                first_val = random_nth_digit(first_len)
            inner_dict['first_value'] = first_val
            inner_dict['second_value'] = second_val
            color_lst = list(colors.keys())
            ran_color = random.choice(color_lst)
            inner_dict['color'] = ran_color
            inner_dict['text'] = colors[ran_color]
            print(random.choice(color_lst))
            questions.append(inner_dict)

        context = {
            'questions': questions,
            'operator': operator[operation.lower()],
            'operation': operation
        }
    else:
        raise Http404('Page was not found.')
    # return redirect(request.META['HTTP_REFERER'])
    return render(request, 'frontend/exam.html', context)
