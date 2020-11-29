from django.conf import settings
import subprocess
from threading import Timer
from learn.models import Person, Level, Progress


def processPythonFile(filename):
    cmd = subprocess.Popen(["python3", "%s/%s" % (settings.MEDIA_ROOT, filename)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    timer = Timer(0.5, lambda process: process.kill(), [cmd])
    try:
        timer.start()
        stdout, _ = cmd.communicate()
    finally:
        timer.cancel()

    output = stdout.strip().decode("utf-8").strip('\x00')
    return output


def checkCode(code, expectedOutput):
    with open( "%s/%s.py" % (settings.MEDIA_ROOT, "userID_editor"), "w") as file:
        file.write(code)
    if "import" in code:
        return "Error. Please do not use any external packages in your code."
    if "while True" in code:
        return "Error. You don't want to use an infinite loop. Try again."
    output = processPythonFile("userID_editor.py")
    return output


def convertTerminalToHTML(output):
    formatted = output.split("\n")
    return "<br>".join(formatted)

def compareCode(code1, code2):
    code1Break = [x for x in code1.split("\n") if x]
    code2Break = [x.replace("\r", "") for x in code2.split("\n") if x]
    # print(code1Break, code2Break)
    return code1Break == code2Break
    
def getPerson(request):
    username = request.user.username
    if request.user.is_authenticated:
        if Person.objects.filter(username=username).exists():
            return Person.objects.get(username=username)
        p = Person(username=username)
        p.save()
        return p

def is_high_enough_level(person, level):
    if person.topLevel.pk >= level:
        return True
    return False