# Generated by Django 5.0.6 on 2024-05-17 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smallblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]