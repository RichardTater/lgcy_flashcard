# Generated by Django 4.2.6 on 2023-10-13 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Flashcards',
        ),
    ]