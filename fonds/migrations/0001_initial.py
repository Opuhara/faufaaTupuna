# Generated by Django 5.1.1 on 2024-09-05 17:58

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveFonds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('date', models.CharField(help_text='e.g. 1945-1990', max_length=50)),
                ('level_of_description', models.CharField(choices=[('Fonds', 'Fonds'), ('Series', 'Series'), ('File', 'File'), ('Item', 'Item')], default='Fonds', help_text='e.g. 1945-1990', max_length=20)),
                ('creator', models.CharField(max_length=255)),
                ('administrative_history', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('appraisal_destroy', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('conditions_governing_access', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('conditions_governing_reproduction', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('language_of_material', models.CharField(blank=True, max_length=100, null=True)),
                ('physical_characteristics', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('location_of_originals', models.CharField(blank=True, max_length=255, null=True)),
                ('related_units_of_description', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('notes', markdownx.models.MarkdownxField(blank=True, null=True)),
                ('archivist_name', models.CharField(max_length=255)),
                ('date_of_description', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
