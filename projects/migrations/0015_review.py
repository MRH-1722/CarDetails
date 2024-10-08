# Generated by Django 5.0.7 on 2024-09-23 06:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_detail_options_delete_body_detail'),
        ('users', '0007_remove_profile_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.detail')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'unique_together': {('owner', 'detail')},
            },
        ),
    ]
