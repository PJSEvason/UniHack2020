from django.shortcuts import render
from django.http import HttpResponse
from learn.forms import writeCodeForm
from learn.models import Person, Level, Progress, Hint
from django.contrib.auth.decorators import login_required, user_passes_test
from .common import checkCode, convertTerminalToHTML, processPythonFile, getPerson, is_high_enough_level, compareCode

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

# shows their name and all levels with their title
@login_required
def menuScreenView(request):
    person = getPerson(request)
    levels = Level.objects.all()
    displayLevels = []
    maxLevelAvailable = person.topLevel.pk
    for level in levels:
        if level.pk <= maxLevelAvailable:
            displayLevels.append({'num': level.pk, 'title': level.title, 'available': True})
        else:
            displayLevels.append({'num': level.pk, 'title': level.title, 'available': False})
        
    return render(
        request,
        'menu.html',
        {'name': "%s %s" % (person.first_name, person.last_name), 'levels': displayLevels}
    )

# shows the level number, the title and summary
@login_required
def levelTitleScreenView(request, level_num):
    person = getPerson(request)
    if not is_high_enough_level(person, level_num):
        return HttpResponse("Sorry mate/ NOT TODAY")
    level = Level.objects.get(pk=level_num)
    return render(
        request,
        'levelTitleScreen.html',
        {'title': level.title, 'summary': level.summary, 'num': level.pk}
    )

# editor where they can write the code - add validation to check level exists!!
@login_required
def levelEditorView(request, level_num):
    person = getPerson(request)
    if not is_high_enough_level(person, level_num):
        return HttpResponse("Sorry mate/ NOT TODAY")
    level = Level.objects.get(pk=level_num)
    form = writeCodeForm() # change form
    output = "Run your code to see the results."
    expectedOutput = level.expectedOutput
    complete = False
    if request.POST:
        form = writeCodeForm(request.POST)
        if form.is_valid():
            progressObj = form.save(commit=False)
            progressObj.person = person
            progressObj.level = level
            output = checkCode(form.cleaned_data['code'], expectedOutput)
            progressObj.isCorrect = output == expectedOutput
            progressObj.save()
            isCorrect = compareCode(output, expectedOutput)
            if isCorrect:
                if Level.objects.filter(pk=level_num+1).exists():
                    person.topLevel=Level.objects.get(pk=level_num+1)
                    person.save()
                else:
                    complete = True
    return render(
        request,
        'index.html',
        {'form': form, 'output': convertTerminalToHTML(output), "correct": compareCode(output, expectedOutput), "next_num": level_num+1, "complete": complete, "instructions": level.instructions, "title": level.title}
    )

