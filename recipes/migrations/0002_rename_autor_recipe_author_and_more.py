# Generated by Django 5.1.5 on 2025-02-06 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='categoty',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
    ]
