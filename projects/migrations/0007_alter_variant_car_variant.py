# Generated by Django 5.0.7 on 2024-07-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_body_detail_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='car_variant',
            field=models.CharField(choices=[('simple', 'Simple Oriel'), ('oriel', 'oriel prosmectic'), ('oriel ivtec', 'Oriel ivTec'), ('UG iv', 'UG Oriel ivTec'), ('UG p', 'UG Oriel Pros'), ('xli', 'XLI'), ('gli', 'GLI'), ('grande', 'Grande'), ('altis', 'Altis'), ('l', 'L'), ('s', 'S'), ('g', 'G')], max_length=20),
        ),
    ]
