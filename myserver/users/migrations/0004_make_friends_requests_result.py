# Generated by Django 2.2.2 on 2019-07-08 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190707_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='make_friends_requests',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]