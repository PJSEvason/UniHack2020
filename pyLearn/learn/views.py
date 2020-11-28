from django.shortcuts import render
from django.http import HttpResponse
import subprocess
from django.conf import settings

# Create your views here.
def index(request):
    processPythonFile("example.py")
    return render(
        request,
        'index.html',
        {}
    )

def processPythonFile(filename):
    # save their files locally :)
    print(settings.MEDIA_ROOT)
    cmd = subprocess.Popen(["python3", "%s/%s" % (settings.MEDIA_ROOT, filename)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in cmd.stdout.readlines():
        line = line.strip().decode("utf-8").strip('\x00')
        print(line)