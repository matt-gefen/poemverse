# Generated by Django 3.2.9 on 2021-11-26 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_poem_lines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='linecount',
        ),
    ]
