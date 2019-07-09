# Generated by Django 2.2.2 on 2019-07-09 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0025_auto_20190708_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='assessment',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='users_liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='work_load',
            field=models.IntegerField(),
        ),
    ]
