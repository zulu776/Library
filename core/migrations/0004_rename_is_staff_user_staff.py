# Generated by Django 3.2 on 2022-03-22 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_staff_user_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_staff',
            new_name='staff',
        ),
    ]
