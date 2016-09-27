# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import popoteafrica.models


class Migration(migrations.Migration):

    dependencies = [
        ('popoteafrica', '0004_auto_20160912_2203'),
    ]

    operations = [
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
