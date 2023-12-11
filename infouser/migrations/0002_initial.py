# Generated by Django 5.0a1 on 2023-11-03 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infouser', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='emissor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_sent_not', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_received_not', to=settings.AUTH_USER_MODEL),
        ),
    ]
