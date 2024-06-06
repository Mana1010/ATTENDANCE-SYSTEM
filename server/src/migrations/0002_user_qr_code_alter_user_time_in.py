# Generated by Django 5.0.6 on 2024-06-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qr_code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='time_in',
            field=models.DateField(),
        ),
    ]
