# Generated by Django 5.1.5 on 2025-02-06 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_rename_prepation_steps_recipe_preparation_steps_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_steps',
            new_name='prepation_steps',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_steps_is_html',
            new_name='prepation_steps_is_html',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_time',
            new_name='prepation_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_time_unit',
            new_name='prepation_time_unit',
        ),
    ]
