# Generated by Django 5.0a1 on 2023-11-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_avatar_user_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='upload',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
