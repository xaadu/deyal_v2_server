# Generated by Django 4.2.4 on 2023-09-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.CharField(primary_key=True, serialize=False)),
                ('full_name', models.CharField()),
                ('photo_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
