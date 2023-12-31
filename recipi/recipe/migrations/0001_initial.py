# Generated by Django 4.2.4 on 2023-08-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeName', models.CharField(max_length=100)),
                ('recipeCode', models.ImageField(upload_to='')),
                ('recipeDetils', models.TextField()),
                ('recipeImage', models.ImageField(upload_to='recipe_img')),
            ],
        ),
    ]
