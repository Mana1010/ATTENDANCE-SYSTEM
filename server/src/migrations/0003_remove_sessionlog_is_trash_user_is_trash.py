# Generated by Django 5.0.6 on 2024-06-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_remove_user_is_trash_sessionlog_is_trash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionlog',
            name='is_trash',
        ),
        migrations.AddField(
            model_name='user',
            name='is_trash',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]