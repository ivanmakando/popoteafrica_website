# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import popoteafrica.models


class Migration(migrations.Migration):

    dependencies = [
        ('popoteafrica', '0016_auto_20160915_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllSafariTripsForOpenDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depature_dates', models.DateField(help_text=b'The day trip will start')),
                ('return_dates', models.DateField(help_text=b'The day trip will end')),
                ('price', models.IntegerField(default=b'1000', help_text=b'Fill in the price for this trip')),
                ('trip_duration', models.IntegerField(default=0, help_text=b'Fill in How many days the trip would take')),
                ('trip_name', models.CharField(default=b'fill in about Trip Name', max_length=1000)),
                ('trip_route', models.ForeignKey(help_text=b'Put a Safari Trip Only', null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route')),
            ],
        ),
        migrations.RemoveField(
            model_name='thesafaricollection',
            name='trip_route',
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
        migrations.AlterField(
            model_name='bookingsforsafariopendates',
            name='trip_booked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.AllSafariTripsForOpenDates'),
        ),
        migrations.DeleteModel(
            name='TheSafariCollection',
        ),
    ]