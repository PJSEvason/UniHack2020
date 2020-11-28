# Generated by Django 3.1.3 on 2020-11-28 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=250)),
                ('instructions', models.CharField(max_length=500)),
                ('expectedOutput', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('topLevel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.level', verbose_name='most recent level')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('isCorrect', models.BooleanField(default=False)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.level', verbose_name='this level')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.person', verbose_name='this person')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=250)),
                ('code_sample', models.CharField(max_length=250)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.level', verbose_name='hint for this level')),
            ],
        ),
    ]
