# Generated by Django 3.1.7 on 2021-04-13 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='category',
        ),
    ]
