# Generated by Django 3.2 on 2022-03-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_manage', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='jacome', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='jacobo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='added',
            field=models.DateField(default='2022-02-28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='español', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.CharField(default='ahora', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.CharField(default='hoñla', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='hola', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='added',
            field=models.DateField(default='2022-02-28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='language',
            field=models.CharField(default='español', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='number_of_pages',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='published',
            field=models.CharField(default='ahora', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='subject',
            field=models.CharField(default='hola', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookitem',
            name='title',
            field=models.CharField(default='hola', max_length=100),
            preserve_default=False,
        ),
    ]
