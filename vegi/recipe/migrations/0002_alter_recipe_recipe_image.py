# Generated by Django 5.0.1 on 2024-01-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_image",
            field=models.ImageField(upload_to="recipeImages"),
        ),
    ]
