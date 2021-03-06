# Generated by Django 2.2.2 on 2019-06-21 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='done',
            field=models.ManyToManyField(related_name='done', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='assessment',
            field=models.IntegerField(choices=[(1, 'Problem sets'), (2, 'Projects'), (3, 'Presentations'), (4, 'Exams'), (5, 'Papers')], default=2),
        ),
        migrations.AlterField(
            model_name='review',
            name='class_size',
            field=models.IntegerField(choices=[(1, 'Small:1-10'), (2, 'Medium:10-20'), (3, 'Large:20+')], default=2),
        ),
        migrations.AlterField(
            model_name='review',
            name='diff_level',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard'), (4, 'Insane')], default=2),
        ),
        migrations.AlterField(
            model_name='review',
            name='work_load',
            field=models.IntegerField(choices=[(1, 'Light:<=3 hours/week'), (2, 'Medium:<=6 hours/week'), (3, 'Heavy:<=10 hours/week'), (4, 'Insane:>10 hours/week')], default=2),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('sub', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('anonymous', models.BooleanField(choices=[(False, 'False'), (True, 'True:Your username is NOT recorded.You CANNOT modify this review later!!')], default=False)),
                ('response', models.CharField(max_length=200)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Department')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.Department'),
        ),
    ]
