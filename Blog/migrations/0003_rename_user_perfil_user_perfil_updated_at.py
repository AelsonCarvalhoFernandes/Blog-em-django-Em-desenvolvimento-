# Generated by Django 4.1.5 on 2023-01-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='User',
            new_name='user',
        ),
        migrations.AddField(
            model_name='perfil',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
