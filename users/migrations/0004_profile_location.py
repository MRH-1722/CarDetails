# Generated by Django 5.0.7 on 2024-08-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
