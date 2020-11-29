from django.shortcuts import render
from django.http import HttpResponse
from learn.forms import writeCodeForm, createNewPersonForm
from learn.models import Person, Level, Progress
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .common import checkCode, convertTerminalToHTML, processPythonFile, getPerson, is_high_enough_level, compareCode
from django.urls import reverse
from django.shortcuts import redirect

def userCreationView(request):
    form1 = UserCreationForm()
    form2 = createNewPersonForm()
    if request.POST:
        form1 = UserCreationForm(request.POST)
        form2 = createNewPersonForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit = False)
            person = form2.save(commit=False)
            person.username = user.username
            person.topLevel = Level.objects.get(pk=1)
            user.save()
            person.save()
            loginUser = authenticate(username = form1.cleaned_data['username'], password=form1.cleaned_data['password1'],)
            login(request, loginUser)
            return redirect(reverse('menu'))
    return render(
        request,
        'registration/signup.html',
        {'form1': form1, 'form2': form2}
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
                if person.topLevel.pk == level_num:
                    person.topLevel=Level.objects.get(pk=level_num+1)
                person.save()
                if not Level.objects.filter(pk=level_num+1).exists():
                    complete = True
    return render(
        request,
        'index.html',
        {'form': form, 'output': convertTerminalToHTML(output), "correct": compareCode(output, expectedOutput), "next_num": level_num+1, "complete": complete, "instructions": convertTerminalToHTML(level.instructions), "title": level.title}
    )

