# Generated by Django 2.2.3 on 2019-09-10 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarbCount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
    ]