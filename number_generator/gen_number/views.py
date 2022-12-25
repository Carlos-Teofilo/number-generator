from django.shortcuts import render
from random import randint

from . import forms


def get_numbers(request):
    context = {
        'error_messages': [],
        'form': forms.GenNumbersForm(),
    }

    if request.method == 'POST':
        form = forms.GenNumbersForm(request.POST or None)
        begin = int(request.POST['begin'])
        end = int(request.POST['end'])
        qtd = int(request.POST['qtd'])
        unique = True if 'unique' in request.POST else False

        if qtd <= 0:
            context['error_messages'].append('A quantidade de números não pode ser menor ou igual a 0')
        if begin > end:
            context['error_messages'].append('O valor inicial não pode ser maior que o final')
        if qtd > (end - begin) + 1 and unique:
            context['error_messages'].append('Essa opção não é possível para valores únicos')
        if context['error_messages']:
            return render(request, 'gen_numbers/index.html', context)

        if form.is_valid():
            n = random_numbers(begin, end, qtd, unique)
            context['numbers'] = n

    return render(request, 'gen_numbers/index.html', context)


def random_numbers(begin, end, qtd, unique):
    numbers = []

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
