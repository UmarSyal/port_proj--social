# Generated by Django 2.2.5 on 2019-12-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200),
        ),
    ]
