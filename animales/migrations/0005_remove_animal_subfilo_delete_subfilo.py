# Generated by Django 4.1.7 on 2023-03-12 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0004_alter_subfilo_subfilo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='subfilo',
        ),
        migrations.DeleteModel(
            name='Subfilo',
        ),
    ]
