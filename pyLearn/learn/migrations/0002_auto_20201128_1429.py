# Generated by Django 3.1.3 on 2020-11-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hint',
            name='body',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='hint',
            name='code_sample',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='level',
            name='expectedOutput',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='level',
            name='instructions',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='level',
            name='summary',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='progress',
            name='code',
            field=models.TextField(max_length=1000),
        ),
    ]