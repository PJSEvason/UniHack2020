from django.conf import settings
import subprocess

def processPythonFile(filename):
    print(settings.MEDIA_ROOT)
    cmd = subprocess.Popen(["python3", "%s/%s" % (settings.MEDIA_ROOT, filename)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in cmd.stdout.readlines():
        line = line.strip().decode("utf-8").strip('\x00')
        output.append(line)
    return "\n".join(output)


def checkCode(code, expectedOutput):
    print(code, expectedOutput)
    with open( "%s/%s.py" % (settings.MEDIA_ROOT, "userID_editor"), "w") as file:
        file.write(code)
    if "import" in code:
        return "Error. Please do not use any external packages in your code."
    output = processPythonFile("userID_editor.py")
    return output


def convertTerminalToHTML(output):
    formatted = output.split("\n")
    return "<br>".join(formatted)