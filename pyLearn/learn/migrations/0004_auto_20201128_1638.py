# Generated by Django 3.1.3 on 2020-11-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_person_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(default='Username', max_length=20),
        ),
    ]