# Generated by Django 5.0.1 on 2024-01-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_marka_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='marka',
        ),
        migrations.DeleteModel(
            name='Marka',
        ),
    ]