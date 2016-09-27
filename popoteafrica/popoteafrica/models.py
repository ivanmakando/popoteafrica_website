from django.db import models
from django.contrib.auth.models import User
from time import time
from django.utils import timezone
#this is the directory of the images that are uploaded in the admin, the function also defines the format of the name
def gallery_images(instance, filename):
    return "gallery/%s_%s" %(str(time()).replace('.', '_'), filename)

#this class defines the model that contains the contents to pack to treck kilimanjaro
class KiliPackList(models.Model):
    list_picture = models.ImageField(upload_to = gallery_images, null = True, blank = True, help_text="Please use the image of width: 275, Height: 426")
    list_heading = models.CharField(max_length = 100, null = True, blank = True, help_text = "Put the heading of the list")
    item1 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item2 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item3 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item4 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item5 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item6 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item7 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item8 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item9 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item10 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item11 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item12 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item13 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item14 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item15 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")

    def __unicode__(self):
           return  self.list_heading
#this class defines the model that contains the contents to pack for a safari
class SafariPackList(models.Model):
    list_picture = models.ImageField(upload_to = gallery_images, null = True, blank = True, help_text="Please use the image of width: 275, Height: 426")
    list_heading = models.CharField(max_length = 100, null = True, blank = True, help_text = "put the name of tis list")
    item1 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item2 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item3 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item4 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item5 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item6 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item7 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item8 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item9 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item10 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item11 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item12 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item13 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item14 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")
    item15 = models.CharField(max_length = 100, null = True, blank = True, help_text = "mention an item here")

    def __unicode__(self):
           return  self.list_heading
#this class defines the model that contains the contetents of animal migrations
class AnimalMigrations(models.Model):
    head = models.CharField(max_length = 1000, help_text = "put the heading here")
    subtitle = models.CharField(max_length = 1000, null = True, blank = True, help_text = "put a subheading if available or leave blank")
    body_contents = models.CharField(max_length = 10000, help_text = "put the contents of the heading here")

    def __unicode__(self):
           return  self.head
#this class defines the model that contains the contents of tips for climbing kilimanjaro
class ClimbKilimanjaroTips(models.Model):
    head = models.CharField(max_length = 1000, null = True, blank = True, help_text = "put the heading here")
    body_contents = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here")
    body_contents2 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents3 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents4 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents5 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents6 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents7 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents8 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")
    body_contents9 = models.CharField(max_length = 10000, null = True, blank = True, help_text = "put contents of the heading here or leave blank")

    def __unicode__(self):
           return  self.head
#class for hoe to plan a safari
class HowToPlanASafari(models.Model):
    head = models.CharField(max_length = 1000, help_text = "put the heading here")
    body_contents = models.CharField(max_length = 10000, help_text = "put contents of the heading here")
    def __unicode__(self):
           return  self.head
#class for FAQ
class FAQ(models.Model):
    head = models.CharField(max_length = 1000, help_text = "put the heading here")
    faq_body = models.CharField(max_length = 10000, help_text = "put contents of the heading here")

    def __unicode__(self):
           return  self.head

#this class is for booking a single trip e.g. bookin lemosho trip only
class BookingsForIndividualTrip(models.Model):
    fir_name = models.CharField(max_length = 50)
    las_name = models.CharField(max_length = 50)
    email_add = models.EmailField()
    phone_no = models.IntegerField()
    pref_destination = models.CharField(max_length = 50)
    adults_no = models.IntegerField(default = 0)
    children_no = models.IntegerField(default = 0)
    special_requests = models.CharField(max_length = 1000)

    def __unicode__(self):
           return  self.fir_name + " " + self.las_name

#this is a class for all pages
class Route(models.Model):
    route_name = models.CharField(max_length = 1000, help_text="Put The Heading/ name of the Route or the page")
    about_route = models.CharField(max_length = 10000, help_text="Put The contents of the Route or the page")
    route_background = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 1600, Height: 596")

    def __unicode__(self):
       return self.route_name

#class foe terms and conditions
class TermsAndConditions(models.Model):
    head = models.CharField(max_length = 1000, help_text="Put The Heading/ name")
    terms_body = models.CharField(max_length = 10000, help_text="Put The contents here")

    def __unicode__(self):
           return  self.head

#class for guides information
class AboutGuides(models.Model):
    head = models.CharField(max_length = 1000, help_text="Put The Heading/ name")
    about_guides_body = models.CharField(max_length = 10000, help_text="Put The contents here")

    def __unicode__(self):
           return  self.head

#class to define all one day programmes trips
class AllOneDayProgramTripsForOpenDates(models.Model):
    trip_route = models.ForeignKey('Route', null = True, help_text = "Put a One Day Program Trip Only")
    depature_date = models.DateField(help_text = "Put a the date that the trip is departing")
    return_date = models.DateField(help_text = "Put a the date that the trip is returning")
    price = models.IntegerField(help_text = "Put a the price of this trip")
    trip_duration = models.IntegerField(default = 0, help_text = "Put a the number of days that will be spent in this trip")
    about_trip = models.CharField(max_length = 10000, default = "fill in about Trip")
    trip_name = models.CharField(max_length = 1000, default = "fill in about Trip Name")

    def __unicode__(self):
           return  self.trip_name

#booking for one day Program
class BookingsOneDayProgramOpenDate(models.Model):
    fi_name = models.CharField(max_length = 50)
    la_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    prefered_destination = models.CharField(max_length = 50)
    adults_number = models.IntegerField(default = 0)
    children_number = models.IntegerField(default = 0)
    special_request = models.CharField(max_length = 1000)
    trip_booked = models.ForeignKey(AllOneDayProgramTripsForOpenDates, null = True)

    def __unicode__(self):
           return  self.fi_name + " " + self.la_name




#class defined all zanzibar trips for open dates
class AllZanzibarTripsForOpenDates(models.Model):
    trip_route = models.ForeignKey('Route', null = True, help_text = "Put a Zanzibar Trip Only",)
    depature_date = models.DateField(help_text = "Put a the date that the trip is departing")
    return_date = models.DateField(help_text = "Put a the date that the trip is returning")
    price = models.IntegerField(help_text = "Put a the price of this trip")
    trip_duration = models.IntegerField(default = 0, help_text = "Put a the number of days that will be spent in this trip")
    about_trip = models.CharField(max_length = 10000, default = "fill in about Trip")
    trip_name = models.CharField(max_length = 1000, default = "fill in about Trip Name")

    def __unicode__(self):
           return  self.trip_name

#booking for zanzibar trips one day
class BookingsForZanzibarOpenDate(models.Model):
    fi_name = models.CharField(max_length = 50)
    la_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    prefered_destination = models.CharField(max_length = 50)
    adults_number = models.IntegerField(default = 0)
    children_number = models.IntegerField(default = 0)
    special_request = models.CharField(max_length = 1000)
    trip_booked = models.ForeignKey(AllZanzibarTripsForOpenDates, null = True)

    def __unicode__(self):
           return  self.fi_name + " " + self.la_name

#mountain trips plans for open dates
class AllMountainTripsForOpenDates(models.Model):
    trip_route = models.ForeignKey('Route', null = True, help_text = "Put a Mountain Route Only")
    depature_date = models.DateField(help_text = "Put a the date that the trip is departing")
    return_date = models.DateField(help_text = "Put a the date that the trip is returning")
    price = models.IntegerField(help_text = "Put a the price of this trip")
    trip_duration = models.IntegerField(default = 0, help_text = "Put a the number of days that will be spent in this trip")
    about_trip = models.CharField(max_length = 10000, default = "fill in about Trip")
    trip_name = models.CharField(max_length = 1000, default = "fill in about Trip Name")

    def __unicode__(self):
           return  self.trip_name

#booking for mountain trips open dates
class BookingsMountainOpenDates(models.Model):
    fi_name = models.CharField(max_length = 50)
    la_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    prefered_destination = models.CharField(max_length = 50)
    adults_number = models.IntegerField(default = 0)
    children_number = models.IntegerField(default = 0)
    special_request = models.CharField(max_length = 1000)
    trip_booked = models.ForeignKey(AllMountainTripsForOpenDates, null = True)

    def __unicode__(self):
           return  self.fi_name + " " + self.la_name

#all safari trips plans for open dates
class AllSafariTripsForOpenDates(models.Model):
    trip_route = models.ForeignKey('Route', null = True, help_text = "Put a Safari Trip Only")
    depature_dates = models.DateField(help_text = "The day trip will start")
    return_dates = models.DateField(help_text = "The day trip will end")
    price = models.IntegerField(default = "1000", help_text = "Fill in the price for this trip")
    trip_duration = models.IntegerField(default = 0, help_text = "Fill in How many days the trip would take")
    trip_name = models.CharField(max_length = 1000, default = "fill in about Trip Name")

    def __unicode__(self):
           return  self.trip_name

#booking fr safari trips in open dates
class BookingsForSafariOpenDates(models.Model):
    fi_name = models.CharField(max_length = 50)
    la_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    prefered_destination = models.CharField(max_length = 50)
    adults_number = models.IntegerField(default = 0)
    children_number = models.IntegerField(default = 0)
    special_request = models.CharField(max_length = 1000)
    trip_booked = models.ForeignKey(AllSafariTripsForOpenDates, null = True)

    def __unicode__(self):
           return  self.fi_name + " " + self.la_name

#all safari plans that occurs in the chart according to the days
class SafariPlansForTheChart(models.Model):
    trip_days = models.IntegerField(default = 0, help_text = "Put The number of days for this plan")
    trip_price = models.IntegerField(default = 1000, null = True, blank = True, help_text = "Put The price for this plan")
    days_arusha_park = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at arusha national park for this plan")
    hours_arusha_park = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at arusha national park for this plan")
    days_lake_manyara = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at lake manyara national park for this plan")
    hours_lake_manyara = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at lake manyara national park for this plan")
    days_lake_eyasi = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at lake eyasi national park for this plan")
    hours_lake_eyasi = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at lake eyasi national park for this plan")
    days_serengeti = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at serengeti national park for this plan")
    hours_serengeti = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at serengeti national park for this plan")
    days_ngorongoro = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at Ngorongoro Crater national park for this plan")
    hours_ngorongoro = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at Ngorongoro Crater national park for this plan")
    days_tarangire = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at Tarangire Crater national park for this plan")
    hours_tarangire = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at Tarangire Crater national park for this plan")
    days_cultural_vilages = models.CharField(max_length = 100, default = 0, help_text = "Put The number of days at Cultural Vilage for this plan")
    hours_cultural_vilages = models.CharField(max_length = 100, default = 0, help_text = "Put The hours spent at Cultural Vilage for this plan")

    def __unicode__(self):
           return  str(self.trip_days)

#bookings for individual safari trips
class BookingsForIndividualSafariTrip(models.Model):
    fi_name = models.CharField(max_length = 50)
    la_name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    prefered_destination = models.CharField(max_length = 50)
    adults_number = models.IntegerField(default = 0)
    children_number = models.IntegerField(default = 0)
    special_request = models.CharField(max_length = 1000)
    trip_booked = models.ForeignKey(SafariPlansForTheChart, null = True)

    def __unicode__(self):
           return  self.fi_name + " " + self.la_name


class TripSixDayInfo(models.Model):
    name_of_route = models.CharField(max_length = 100)
    trip_route_name = models.ForeignKey(Route)
    day = models.IntegerField()
    start_at = models.CharField(max_length = 100)
    meter_altitude_start = models.IntegerField()
    ft_altitude_start = models.IntegerField()
    finish_at = models.CharField(max_length = 100)
    meter_altitude_finish = models.IntegerField()
    ft_altitude_finish = models.IntegerField()
    min_time_required  = models.IntegerField()
    max_time_required  = models.IntegerField(default = 0)
    distance_covered_km = models.IntegerField()
    distance_covered_ft = models.IntegerField()

    def __unicode__(self):
           return  self.name_of_route


class TripSevenDayInfo(models.Model):
    name_of_route = models.CharField(max_length = 100)
    trip_route_name = models.ForeignKey(Route)
    day = models.IntegerField()
    start_at = models.CharField(max_length = 100)
    meter_altitude_start = models.IntegerField()
    ft_altitude_start = models.IntegerField()
    finish_at = models.CharField(max_length = 100)
    meter_altitude_finish = models.IntegerField()
    ft_altitude_finish = models.IntegerField()
    min_time_required  = models.IntegerField()
    max_time_required  = models.IntegerField(default = 0)
    distance_covered_km = models.IntegerField()
    distance_covered_ft = models.IntegerField()

    def __unicode__(self):
           return  self.name_of_route


class Feed(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    nick_name = models.CharField(max_length = 30)
    feed_body = models.CharField(max_length = 1000)
    pub_date = models.DateTimeField (auto_now_add=True)

    def __unicode__(self):
           return "A feedback from: " + "@" + self.nick_name

class Contact(models.Model):
    f_name = models.CharField(max_length = 30,)
    l_name = models.CharField(max_length = 30,)
    email_addr = models.EmailField()
    phone_number = models. IntegerField()
    your_message = models.CharField(max_length = 10000)
    time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
           return "contact message from: " + self.f_name +" "+ self.l_name


def file_location(instance, filename):
    return "banner_video/%s_%s" %(str(time()).replace('.', '_'), filename)

class MainPageContent(models.Model):
    imported_by = models.ForeignKey(User)
    about_popoteafrica = models.CharField(max_length = 10000, default = "Put Something from Admin")
    banner_video = models.FileField(upload_to = file_location, null = True)


def activity_image_location(instance, filename):
    return "activity_images/%s_%s" %(str(time()).replace('.', '_'), filename)

class Activities(models.Model):
    route = models.ForeignKey(Route, null = True)
    activity_name = models.CharField(max_length = 100, null = True, blank = True)
    activity_1_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_1 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_1 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_2_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_2 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_2 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_3_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_3 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_3 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_4_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_4 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_4 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_5_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_5 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_5 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_6_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_6 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_6 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_7_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_7 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_7 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_8_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_8 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_8 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_9_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_9 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_9 = models.CharField(max_length = 1000, null = True, blank = True)

    def __unicode__(self):
           return  self.activity_name

class Gallery(models.Model):
    gallery_text = models.CharField(max_length = 1000, default = 'Gallery text, upload from Admin')
    gallery_image1 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image2 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image3 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image4 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image5 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image6 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image7 = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    gallery_image8 = models.ImageField(upload_to = gallery_images, null = True, blank=True)

class GeneralGallery(models.Model):
    gallery_intro = models.CharField(max_length = 1000, null = True)
    gallery_place = models.CharField(max_length = 100, null = True)
    picture_one = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_one = models.CharField(max_length = 100, null = True)
    picture_content_one = models.CharField(max_length = 1000, null = True)
    picture_two = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_two = models.CharField(max_length = 100, null = True)
    picture_content_two = models.CharField(max_length = 1000, null = True)
    picture_tree = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_three = models.CharField(max_length = 100, null = True)
    picture_content_three = models.CharField(max_length = 1000, null = True)
    picture_four = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_four = models.CharField(max_length = 100, null = True)
    picture_content_four = models.CharField(max_length = 1000, null = True)
    picture_five = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_five = models.CharField(max_length = 100, null = True)
    picture_content_five = models.CharField(max_length = 1000, null = True)
    picture_six = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_six = models.CharField(max_length = 100, null = True)
    picture_content_six = models.CharField(max_length = 1000, null = True)
    picture_seven = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_seven = models.CharField(max_length = 100, null = True)
    picture_content_seven = models.CharField(max_length = 1000, null = True)
    picture_eight = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_eight = models.CharField(max_length = 100, null = True)
    picture_content_eight = models.CharField(max_length = 1000, null = True)

    def __unicode__(self):
           return  self.gallery_place

class TripGallery(models.Model):
    trip_name = models.ForeignKey(Route)
    trip_introduction = models.CharField(max_length = 10000)
    picture_one = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 380, Height: 568")
    picture_content_one = models.CharField(max_length = 1000, null = True)
    picture_two = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 380, Height: 568")
    picture_content_two = models.CharField(max_length = 1000, null = True)
    picture_three = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 380, Height: 568")
    picture_content_three = models.CharField(max_length = 1000, null = True)

    def __unicode__(self):
           return  self.trip_name.route_name

class BestSellingTrips(models.Model):
    best_selling_intro = models.CharField(max_length = 10000)
    best_selling_body = models.CharField(max_length = 10000)
    picture_one = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_one = models.CharField(max_length = 100, null = True)
    picture_two = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_two = models.CharField(max_length = 100, null = True)
    picture_three = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_three = models.CharField(max_length = 100, null = True)
    picture_four = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_four = models.CharField(max_length = 100, null = True)
    picture_five = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_five = models.CharField(max_length = 100, null = True)
    picture_six = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_six = models.CharField(max_length = 100, null = True)
    picture_seven = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_seven = models.CharField(max_length = 100, null = True)
    picture_eight = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    picture_head_eight = models.CharField(max_length = 100, null = True)
    picture_big = models.ImageField(upload_to = gallery_images, null = True, blank=True)

class OurTeam(models.Model):
    team_introduction = models.CharField(max_length = 10000)
    picture_one = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 380, Height: 568")
    picture_one_name = models.CharField(max_length = 100, null = True)
    picture_one_postition = models.CharField(max_length = 100, null = True)
    picture_content_one = models.CharField(max_length = 1000, null = True)
    picture_two = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 380, Height: 568")
    picture_two_name = models.CharField(max_length = 100, null = True)
    picture_two_postition = models.CharField(max_length = 100, null = True)
    picture_content_two = models.CharField(max_length = 1000, null = True)
    picture_three = models.ImageField(upload_to = gallery_images, null = True, blank=True, help_text="Please use the image of width: 380, Height: 568")
    picture_three_name = models.CharField(max_length = 100, null = True)
    picture_three_postition = models.CharField(max_length = 100, null = True)
    picture_content_three = models.CharField(max_length = 1000, null = True)

class Partners(models.Model):
    route_partener = models.ForeignKey('Route', null = True)
    partner_one_url = models.URLField()
    partner_one_picture = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    partner_two_url = models.URLField()
    partner_two_picture = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    partner_three_url = models.URLField()
    partner_three_picture = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    partner_four_url = models.URLField()
    partner_four_picture = models.ImageField(upload_to = gallery_images, null = True, blank=True)
    partner_five_url = models.URLField()
    partner_five_picture = models.ImageField(upload_to = gallery_images, null = True, blank=True)

    def __unicode__(self):
           return  self.route_partener.route_name


def activity_image_location(instance, filename):
    return "activity_images/%s_%s" %(str(time()).replace('.', '_'), filename)

class ItenearyForSafari(models.Model):
    Heading = models.CharField(max_length = 10000, null = True, blank = True)
    introduction = models.CharField(max_length = 10000, null = True, blank = True)
    activity_1_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_1 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_1 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_1 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_2_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_2 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_2 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_2 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_3_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_3 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_3 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_3 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_4_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_4 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_4 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_4 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_5_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_5 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_5 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_5 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_6_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_6 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_6 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_6 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_7_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_7 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_7 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_7 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_8_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_8 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_8 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_8 = models.CharField(max_length = 1000, null = True, blank = True)
    activity_9_image = models.FileField(upload_to = activity_image_location, default = '/activity_images/default.png')
    activity_head_9 = models.CharField(max_length = 100, null = True, blank = True)
    activity_subtitle_9 = models.CharField(max_length = 100, null = True, blank = True)
    activity_content_9 = models.CharField(max_length = 1000, null = True, blank = True)

    def __unicode__(self):
           return  self.Heading
