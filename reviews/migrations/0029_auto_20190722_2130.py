# Generated by Django 2.2.2 on 2019-07-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0028_auto_20190714_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='done',
        ),
        migrations.RemoveField(
            model_name='review',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='review',
            name='diff_level',
            field=models.IntegerField(blank=True, choices=[(1, 'VeryEasy'), (2, 'Easy'), (3, 'Manageable'), (4, 'Challenging'), (5, 'Suffocating')], null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]