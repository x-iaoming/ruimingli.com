# Generated by Django 2.2.2 on 2019-07-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0023_department_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='class_size',
            field=models.IntegerField(blank=True, choices=[(1, 'Small:1-10'), (2, 'Medium:10-20'), (3, 'Large:20+')], null=True),
        ),
    ]
