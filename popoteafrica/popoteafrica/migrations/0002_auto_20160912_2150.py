# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import popoteafrica.models


class Migration(migrations.Migration):

    dependencies = [
        ('popoteafrica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheSafariCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depature_dates', models.DateField()),
                ('return_dates', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_1_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_2_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_3_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_4_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_5_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_6_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_7_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_8_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
        migrations.AlterField(
            model_name='activities',
            name='activity_9_image',
            field=models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location),
        ),
    ]
