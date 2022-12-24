from django import forms


class GenNumbersForm(forms.Form):
    begin = forms.IntegerField(initial=1, required=True)
    end = forms.IntegerField(initial=100, required=True)
    qtd = forms.IntegerField(initial=10, required=True)
    unique = forms.BooleanField(initial=True, required=None)
