# Generated by Django 5.1.1 on 2024-09-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_movie_flyers_movie_flyer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(default='No description available'),
        ),
    ]
