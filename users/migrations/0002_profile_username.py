# Generated by Django 5.0.7 on 2024-08-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
