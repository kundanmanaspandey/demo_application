# Generated by Django 5.1.1 on 2024-10-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appvariety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
