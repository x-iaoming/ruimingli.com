# Generated by Django 2.2.2 on 2019-07-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0027_auto_20190713_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
        migrations.AlterField(
            model_name='review',
            name='work_load',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
