# Generated by Django 5.0.7 on 2024-07-29 06:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_id_detail_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body_detail',
            fields=[
                ('body_color', models.CharField(max_length=20)),
                ('body_condition', models.CharField(choices=[('rusted', 'Rusted'), ('painted', 'Total Paint'), ('shower', 'Sides shower'), ('Total', 'Total Geniun')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('car_variant', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='variant',
            field=models.ManyToManyField(blank=True, to='projects.variant'),
        ),
    ]
