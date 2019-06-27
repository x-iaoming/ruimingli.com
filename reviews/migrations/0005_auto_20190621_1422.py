# Generated by Django 2.2.2 on 2019-06-21 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20190621_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='college',
        ),
        migrations.AddField(
            model_name='department',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.College'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='done',
            field=models.ManyToManyField(blank=True, related_name='done', to=settings.AUTH_USER_MODEL),
        ),
    ]
