from django.shortcuts import render
from django.http import HttpResponse
from learn.forms import writeCodeForm
from learn.models import Person, Level, Progress, Hint
from .common import checkCode, convertTerminalToHTML

# Create your views here.
def index(request):
    processPythonFile("example.py")
    return render(
        request,
        'index.html',
        {}
    )

def sampleFormView(request):
    form = writeCodeForm() # change form
    output = "Run your code to see the results."
    if request.POST:
        form = writeCodeForm(request.POST)
        if form.is_valid():
            progressObj = form.save(commit=False)
            progressObj.person = Person.objects.all()[0]
            progressObj.level = Level.objects.all()[0]
            expectedOutput = Level.objects.all()[0].expectedOutput
            output = checkCode(form.cleaned_data['code'], expectedOutput)
            progressObj.isCorrect = output == expectedOutput
            # progressObj.save()
    return render(
        request,
        'formExample.html',
        {'form': form, 'output': convertTerminalToHTML(output)}
    )
