# Generated by Django 3.2 on 2022-03-28 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system_manage', '0015_remove_bookitem_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookitem',
            old_name='cuantity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='bookitem',
            name='bar_code',
        ),
        migrations.RemoveField(
            model_name='rack',
            name='description',
        ),
        migrations.AddField(
            model_name='bookitem',
            name='rent_book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
            preserve_default=False,
        ),
    ]
