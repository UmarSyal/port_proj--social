# Generated by Django 2.2.5 on 2019-12-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True),
        ),
    ]
