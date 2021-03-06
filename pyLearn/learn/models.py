from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Level(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(max_length=250)
    instructions = models.TextField(max_length=1000)
    expectedOutput = models.TextField(max_length=500)    

class Person(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    topLevel = models.ForeignKey(Level, on_delete=models.SET_NULL, verbose_name="most recent level", null=True)

class Progress(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="this person")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name="this level")
    code = models.TextField(max_length=1000, default="#Write your code here")
    isCorrect = models.BooleanField(default=False)
