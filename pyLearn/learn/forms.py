from django import forms
from learn.models import Progress

class writeCodeForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['code']
    def __init__(self, *args, **kwargs):
        super(writeCodeForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs.update({
            'id': 'code_editor', 
            'name': 'code_editor'
        })
