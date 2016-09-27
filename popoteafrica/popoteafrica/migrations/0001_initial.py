# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import popoteafrica.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_1_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_1', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_2_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_2', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_3_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_3', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_3', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_4_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_4', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_4', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_5_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_5', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_5', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_6_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_6', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_6', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_7_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_7', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_7', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_8_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_8', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_8', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_9_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_9', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_9', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AllMountainTrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depature_date', models.DateField()),
                ('return_date', models.DateField()),
                ('price', models.IntegerField()),
                ('trip_duration', models.IntegerField(default=0)),
                ('about_trip', models.CharField(default=b'fill in about Trip', max_length=10000)),
                ('trip_name', models.CharField(default=b'fill in about Trip Name', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AllOneDayProgramTrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depature_date', models.DateField()),
                ('return_date', models.DateField()),
                ('price', models.IntegerField()),
                ('trip_duration', models.IntegerField(default=0)),
                ('about_trip', models.CharField(default=b'fill in about Trip', max_length=10000)),
                ('trip_name', models.CharField(default=b'fill in about Trip Name', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AllZanzibarTrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depature_date', models.DateField()),
                ('return_date', models.DateField()),
                ('price', models.IntegerField()),
                ('trip_duration', models.IntegerField(default=0)),
                ('about_trip', models.CharField(default=b'fill in about Trip', max_length=10000)),
                ('trip_name', models.CharField(default=b'fill in about Trip Name', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=1000)),
                ('subtitle', models.CharField(blank=True, max_length=1000, null=True)),
                ('body_contents', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='BestSellingTrips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_selling_intro', models.CharField(max_length=10000)),
                ('best_selling_body', models.CharField(max_length=10000)),
                ('picture_one', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_one', models.CharField(max_length=100, null=True)),
                ('picture_two', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_two', models.CharField(max_length=100, null=True)),
                ('picture_three', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_three', models.CharField(max_length=100, null=True)),
                ('picture_four', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_four', models.CharField(max_length=100, null=True)),
                ('picture_five', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_five', models.CharField(max_length=100, null=True)),
                ('picture_six', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_six', models.CharField(max_length=100, null=True)),
                ('picture_seven', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_seven', models.CharField(max_length=100, null=True)),
                ('picture_eight', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_eight', models.CharField(max_length=100, null=True)),
                ('picture_big', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
            ],
        ),
        migrations.CreateModel(
            name='BookingIndividualTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fir_name', models.CharField(max_length=50)),
                ('las_name', models.CharField(max_length=50)),
                ('email_add', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('pref_destination', models.CharField(max_length=50)),
                ('adults_no', models.IntegerField(default=0)),
                ('children_no', models.IntegerField(default=0)),
                ('special_requests', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BookingsForAMountain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fi_name', models.CharField(max_length=50)),
                ('la_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('prefered_destination', models.CharField(max_length=50)),
                ('adults_number', models.IntegerField(default=0)),
                ('children_number', models.IntegerField(default=0)),
                ('special_request', models.CharField(max_length=1000)),
                ('trip_booked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.AllMountainTrips')),
            ],
        ),
        migrations.CreateModel(
            name='BookingsForOneDayProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fi_name', models.CharField(max_length=50)),
                ('la_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('prefered_destination', models.CharField(max_length=50)),
                ('adults_number', models.IntegerField(default=0)),
                ('children_number', models.IntegerField(default=0)),
                ('special_request', models.CharField(max_length=1000)),
                ('trip_booked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.AllOneDayProgramTrips')),
            ],
        ),
        migrations.CreateModel(
            name='BookingsForZanzibar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fi_name', models.CharField(max_length=50)),
                ('la_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('prefered_destination', models.CharField(max_length=50)),
                ('adults_number', models.IntegerField(default=0)),
                ('children_number', models.IntegerField(default=0)),
                ('special_request', models.CharField(max_length=1000)),
                ('trip_booked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.AllZanzibarTrips')),
            ],
        ),
        migrations.CreateModel(
            name='ClimbKilimanjaroTips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=1000, null=True)),
                ('body_contents', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents2', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents3', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents4', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents5', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents6', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents7', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents8', models.CharField(blank=True, max_length=10000, null=True)),
                ('body_contents9', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('email_addr', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('your_message', models.CharField(max_length=10000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=1000)),
                ('faq_body', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('nick_name', models.CharField(max_length=30)),
                ('feed_body', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_text', models.CharField(default=b'Gallery text, upload from Admin', max_length=1000)),
                ('gallery_image1', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image2', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image3', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image4', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image5', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image6', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image7', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('gallery_image8', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_intro', models.CharField(max_length=1000, null=True)),
                ('gallery_place', models.CharField(max_length=100, null=True)),
                ('picture_one', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_one', models.CharField(max_length=100, null=True)),
                ('picture_content_one', models.CharField(max_length=1000, null=True)),
                ('picture_two', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_two', models.CharField(max_length=100, null=True)),
                ('picture_content_two', models.CharField(max_length=1000, null=True)),
                ('picture_tree', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_three', models.CharField(max_length=100, null=True)),
                ('picture_content_three', models.CharField(max_length=1000, null=True)),
                ('picture_four', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_four', models.CharField(max_length=100, null=True)),
                ('picture_content_four', models.CharField(max_length=1000, null=True)),
                ('picture_five', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_five', models.CharField(max_length=100, null=True)),
                ('picture_content_five', models.CharField(max_length=1000, null=True)),
                ('picture_six', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_six', models.CharField(max_length=100, null=True)),
                ('picture_content_six', models.CharField(max_length=1000, null=True)),
                ('picture_seven', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_seven', models.CharField(max_length=100, null=True)),
                ('picture_content_seven', models.CharField(max_length=1000, null=True)),
                ('picture_eight', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_head_eight', models.CharField(max_length=100, null=True)),
                ('picture_content_eight', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HowToPlanASafari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=1000)),
                ('body_contents', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ItenearyForSafari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heading', models.CharField(blank=True, max_length=10000, null=True)),
                ('introduction', models.CharField(blank=True, max_length=10000, null=True)),
                ('activity_1_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_1', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_1', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_2_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_2', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_2', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_3_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_3', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_3', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_3', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_4_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_4', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_4', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_4', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_5_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_5', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_5', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_5', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_6_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_6', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_6', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_6', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_7_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_7', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_7', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_7', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_8_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_8', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_8', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_8', models.CharField(blank=True, max_length=1000, null=True)),
                ('activity_9_image', models.FileField(default=b'/activity_images/default.png', upload_to=popoteafrica.models.activity_image_location)),
                ('activity_head_9', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_subtitle_9', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_content_9', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KiliPackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_picture', models.ImageField(blank=True, help_text=b'Please use the image of width: 275, Height: 426', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('list_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('item1', models.CharField(blank=True, max_length=100, null=True)),
                ('item2', models.CharField(blank=True, max_length=100, null=True)),
                ('item3', models.CharField(blank=True, max_length=100, null=True)),
                ('item4', models.CharField(blank=True, max_length=100, null=True)),
                ('item5', models.CharField(blank=True, max_length=100, null=True)),
                ('item6', models.CharField(blank=True, max_length=100, null=True)),
                ('item7', models.CharField(blank=True, max_length=100, null=True)),
                ('item8', models.CharField(blank=True, max_length=100, null=True)),
                ('item9', models.CharField(blank=True, max_length=100, null=True)),
                ('item10', models.CharField(blank=True, max_length=100, null=True)),
                ('item11', models.CharField(blank=True, max_length=100, null=True)),
                ('item12', models.CharField(blank=True, max_length=100, null=True)),
                ('item13', models.CharField(blank=True, max_length=100, null=True)),
                ('item14', models.CharField(blank=True, max_length=100, null=True)),
                ('item15', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainPageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_popoteafrica', models.CharField(default=b'Put Something from Admin', max_length=10000)),
                ('banner_video', models.FileField(null=True, upload_to=popoteafrica.models.file_location)),
                ('imported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_introduction', models.CharField(max_length=10000)),
                ('picture_one', models.ImageField(blank=True, help_text=b'Please use the image of width: 380, Height: 568', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_one_name', models.CharField(max_length=100, null=True)),
                ('picture_one_postition', models.CharField(max_length=100, null=True)),
                ('picture_content_one', models.CharField(max_length=1000, null=True)),
                ('picture_two', models.ImageField(blank=True, help_text=b'Please use the image of width: 380, Height: 568', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_two_name', models.CharField(max_length=100, null=True)),
                ('picture_two_postition', models.CharField(max_length=100, null=True)),
                ('picture_content_two', models.CharField(max_length=1000, null=True)),
                ('picture_three', models.ImageField(blank=True, help_text=b'Please use the image of width: 380, Height: 568', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_three_name', models.CharField(max_length=100, null=True)),
                ('picture_three_postition', models.CharField(max_length=100, null=True)),
                ('picture_content_three', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading1', models.CharField(blank=True, max_length=100, null=True)),
                ('contents', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_one_url', models.URLField()),
                ('partner_one_picture', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('partner_two_url', models.URLField()),
                ('partner_two_picture', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('partner_three_url', models.URLField()),
                ('partner_three_picture', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('partner_four_url', models.URLField()),
                ('partner_four_picture', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
                ('partner_five_url', models.URLField()),
                ('partner_five_picture', models.ImageField(blank=True, null=True, upload_to=popoteafrica.models.gallery_images)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=1000)),
                ('about_route', models.CharField(max_length=10000)),
                ('route_background', models.ImageField(blank=True, help_text=b'Please use the image of width: 1600, Height: 596', null=True, upload_to=popoteafrica.models.gallery_images)),
            ],
        ),
        migrations.CreateModel(
            name='SafariIteneary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_days', models.IntegerField(default=0)),
                ('trip_price', models.IntegerField(blank=True, default=1000, null=True)),
                ('days_arusha_park', models.CharField(default=0, max_length=100)),
                ('hours_arusha_park', models.CharField(default=0, max_length=100)),
                ('days_lake_manyara', models.CharField(default=0, max_length=100)),
                ('hours_lake_manyara', models.CharField(default=0, max_length=100)),
                ('days_lake_eyasi', models.CharField(default=0, max_length=100)),
                ('hours_lake_eyasi', models.CharField(default=0, max_length=100)),
                ('days_serengeti', models.CharField(default=0, max_length=100)),
                ('hours_serengeti', models.CharField(default=0, max_length=100)),
                ('days_ngorongoro', models.CharField(default=0, max_length=100)),
                ('hours_ngorongoro', models.CharField(default=0, max_length=100)),
                ('days_tarangire', models.CharField(default=0, max_length=100)),
                ('hours_tarangire', models.CharField(default=0, max_length=100)),
                ('days_cultural_vilages', models.CharField(default=0, max_length=100)),
                ('hours_cultural_vilages', models.CharField(default=0, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SafariPackList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_picture', models.ImageField(blank=True, help_text=b'Please use the image of width: 275, Height: 426', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('list_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('item1', models.CharField(blank=True, max_length=100, null=True)),
                ('item2', models.CharField(blank=True, max_length=100, null=True)),
                ('item3', models.CharField(blank=True, max_length=100, null=True)),
                ('item4', models.CharField(blank=True, max_length=100, null=True)),
                ('item5', models.CharField(blank=True, max_length=100, null=True)),
                ('item6', models.CharField(blank=True, max_length=100, null=True)),
                ('item7', models.CharField(blank=True, max_length=100, null=True)),
                ('item8', models.CharField(blank=True, max_length=100, null=True)),
                ('item9', models.CharField(blank=True, max_length=100, null=True)),
                ('item10', models.CharField(blank=True, max_length=100, null=True)),
                ('item11', models.CharField(blank=True, max_length=100, null=True)),
                ('item12', models.CharField(blank=True, max_length=100, null=True)),
                ('item13', models.CharField(blank=True, max_length=100, null=True)),
                ('item14', models.CharField(blank=True, max_length=100, null=True)),
                ('item15', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_introduction', models.CharField(max_length=10000)),
                ('picture_one', models.ImageField(blank=True, help_text=b'Please use the image of width: 380, Height: 568', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_content_one', models.CharField(max_length=1000, null=True)),
                ('picture_two', models.ImageField(blank=True, help_text=b'Please use the image of width: 380, Height: 568', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_content_two', models.CharField(max_length=1000, null=True)),
                ('picture_three', models.ImageField(blank=True, help_text=b'Please use the image of width: 380, Height: 568', null=True, upload_to=popoteafrica.models.gallery_images)),
                ('picture_content_three', models.CharField(max_length=1000, null=True)),
                ('trip_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route')),
            ],
        ),
        migrations.CreateModel(
            name='TripSevenDayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_route', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('start_at', models.CharField(max_length=100)),
                ('meter_altitude_start', models.IntegerField()),
                ('ft_altitude_start', models.IntegerField()),
                ('finish_at', models.CharField(max_length=100)),
                ('meter_altitude_finish', models.IntegerField()),
                ('ft_altitude_finish', models.IntegerField()),
                ('min_time_required', models.IntegerField()),
                ('max_time_required', models.IntegerField(default=0)),
                ('distance_covered_km', models.IntegerField()),
                ('distance_covered_ft', models.IntegerField()),
                ('trip_route_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route')),
            ],
        ),
        migrations.CreateModel(
            name='TripSixDayInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_route', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('start_at', models.CharField(max_length=100)),
                ('meter_altitude_start', models.IntegerField()),
                ('ft_altitude_start', models.IntegerField()),
                ('finish_at', models.CharField(max_length=100)),
                ('meter_altitude_finish', models.IntegerField()),
                ('ft_altitude_finish', models.IntegerField()),
                ('min_time_required', models.IntegerField()),
                ('max_time_required', models.IntegerField(default=0)),
                ('distance_covered_km', models.IntegerField()),
                ('distance_covered_ft', models.IntegerField()),
                ('trip_route_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route')),
            ],
        ),
        migrations.AddField(
            model_name='partners',
            name='route_partener',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route'),
        ),
        migrations.AddField(
            model_name='allzanzibartrips',
            name='trip_route',
            field=models.ForeignKey(help_text=b'Put a Mountain Route Only', null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route'),
        ),
        migrations.AddField(
            model_name='allonedayprogramtrips',
            name='trip_route',
            field=models.ForeignKey(help_text=b'Put a Mountain Route Only', null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route'),
        ),
        migrations.AddField(
            model_name='allmountaintrips',
            name='trip_route',
            field=models.ForeignKey(help_text=b'Put a Mountain Route Only', null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route'),
        ),
        migrations.AddField(
            model_name='activities',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='popoteafrica.Route'),
        ),
    ]