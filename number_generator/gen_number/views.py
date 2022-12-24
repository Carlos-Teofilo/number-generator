from django.shortcuts import render
from random import randint

from . import forms


def get_numbers(request):
    context = {}

    if request.method == 'POST':
        form = forms.GenNumbersForm(request.POST)
        if form.is_valid():
            n = random_numbers(form.cleaned_data)
            context['numbers'] = n
    
    context['form_gen_numbers'] = forms.GenNumbersForm(),

    return render(request, 'gen_number/index.html', context)


def random_numbers(form_cleaned_data: dict):
    numbers = []
    begin = int(form_cleaned_data['begin'])
    end = int(form_cleaned_data['end'])
    qtd = int(form_cleaned_data['qtd'])
    unique = form_cleaned_data['unique']

    if unique:
        while len(numbers) < qtd:
            n = str(randint(begin, end))
            if n in numbers:
                print(n in numbers)
                continue
            numbers.append(n)
    else:
        while len(numbers) < qtd:
            n = str(randint(begin, end))
            numbers.append(n)
    return numbers
