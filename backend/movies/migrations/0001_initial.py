# Generated by Django 5.0.6 on 2024-06-27 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update Date')),
                ('first_name', models.CharField(help_text='Enter the first name', max_length=100)),
                ('last_name', models.CharField(help_text='Enter the last name', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last update Date')),
                ('title', models.CharField(help_text='Enter the movie title', max_length=255)),
                ('description', models.TextField(help_text='Enter the movie description')),
                ('actors', models.ManyToManyField(help_text='Select actors for this movie', to='movies.actor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
