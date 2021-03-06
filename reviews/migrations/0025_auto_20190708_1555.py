# Generated by Django 2.2.2 on 2019-07-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0024_auto_20190702_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='class_size',
        ),
        migrations.RemoveField(
            model_name='review',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='review',
            name='pre_req',
        ),
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=800),
        ),
    ]
