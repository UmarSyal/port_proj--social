# Generated by Django 2.2.5 on 2019-12-24 10:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_auto_20191223_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
