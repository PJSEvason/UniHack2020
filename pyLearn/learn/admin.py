from django.contrib import admin

# Register your models here.
from .models import Person, Level, Progress, Hint

# access admin page at 127.0.0.1:8000/admin
# user: dev
# password: password

# Register your models here.
admin.site.register(Person)
admin.site.register(Level)
admin.site.register(Progress)
admin.site.register(Hint)