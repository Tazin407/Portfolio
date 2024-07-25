# Generated by Django 5.0.3 on 2024-07-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('link', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(blank=True, max_length=400, null=True)),
                ('name', models.CharField(max_length=150)),
                ('overview', models.TextField(blank=True, null=True)),
                ('live_link', models.URLField(max_length=400)),
                ('github_link', models.URLField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='skills/media')),
            ],
        ),
    ]
