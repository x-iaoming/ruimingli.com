# Generated by Django 2.2.2 on 2019-06-29 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20190629_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='user_name',
        ),
        migrations.AddField(
            model_name='response',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]