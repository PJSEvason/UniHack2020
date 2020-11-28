from django import forms
from learn.models import Progress

class writeCodeForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['code']