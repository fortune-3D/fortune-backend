# Generated by Django 4.2 on 2023-05-19 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortune', '0003_fortune_delete_cookiestand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fortune',
            name='description',
        ),
        migrations.AddField(
            model_name='fortune',
            name='fortune',
            field=models.CharField(default='', max_length=256),
        ),
    ]
