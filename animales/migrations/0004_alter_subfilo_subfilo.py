# Generated by Django 4.1.7 on 2023-03-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0003_alter_subfilo_subfilo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subfilo',
            name='subfilo',
            field=models.CharField(blank=True, default='No subfilo', max_length=255),
        ),
    ]
