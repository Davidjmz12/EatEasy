# Generated by Django 5.0a1 on 2023-11-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infouser', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
