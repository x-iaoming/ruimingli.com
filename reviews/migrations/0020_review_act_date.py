# Generated by Django 2.2.2 on 2019-07-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0019_auto_20190629_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='act_date',
            field=models.DateTimeField(auto_now=True, verbose_name='last active'),
        ),
    ]
