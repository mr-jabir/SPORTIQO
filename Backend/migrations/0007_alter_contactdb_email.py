# Generated by Django 3.2.10 on 2023-02-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_contactdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
