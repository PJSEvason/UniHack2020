from django import forms
from learn.models import Progress, Person

class writeCodeForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['code']


class createNewPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']