# Generated by Django 2.2.2 on 2019-07-03 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userid',
        ),
    ]
