# Generated by Django 3.2 on 2022-03-25 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('system_manage', '0012_auto_20220324_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookitem',
            name='codig_UUID',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
