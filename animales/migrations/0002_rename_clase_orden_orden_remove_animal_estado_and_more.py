# Generated by Django 4.1.7 on 2023-03-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='clase',
            new_name='orden',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
