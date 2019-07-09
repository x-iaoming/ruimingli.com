# Generated by Django 2.2.2 on 2019-07-01 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0020_review_act_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='review',
            name='act_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
