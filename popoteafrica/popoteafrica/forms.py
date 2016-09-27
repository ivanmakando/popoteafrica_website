from django import forms
from django.forms import extras
from popoteafrica.models import *
import re
from time import time


class BookingIndividualForm(forms.ModelForm):
    email_add2 = forms.EmailField()
    special_requests = forms.CharField(widget = forms.Textarea(), required=True,)
    class Meta:
        model = BookingsForIndividualTrip
        fields = ('fir_name','las_name', 'email_add', 'email_add2','phone_no', 'pref_destination', 'adults_no', 'children_no','special_requests',)

    def clean(self):
        cleaned_data = super(BookingIndividualForm, self).clean()
        first_email = cleaned_data.get("email_add")
        second_email = cleaned_data.get("email_add2")

        if first_email and second_email:
            # Only do something if both fields are valid so far.
            if first_email != second_email:
                raise forms.ValidationError(
                    "The Two Emails Entered Didn't Match, Try Again"
                )

            return cleaned_data



class BookingAMountainForm(forms.ModelForm):
    special_request = forms.CharField(widget = forms.Textarea(), required=True,)
    email2 = forms.EmailField()
    class Meta:
        model = BookingsMountainOpenDates
        fields = ('trip_booked','fi_name', 'la_name', 'email','email2', 'phone_number', 'prefered_destination', 'adults_number', 'children_number','special_request')
        exclude = ['trip_booked']


    def clean(self):
        cleaned_data = super(BookingAMountainForm, self).clean()
        first_email = cleaned_data.get("email")
        second_email = cleaned_data.get("email2")

        if first_email and second_email:
            # Only do something if both fields are valid so far.
            if first_email != second_email:
                raise forms.ValidationError(
                    "The Two Emails Entered Didn't Match, Try Again"
                )

            return cleaned_data


class BookingsForTheSafariCollectionForm(forms.ModelForm):
    special_request = forms.CharField(widget = forms.Textarea(), required=True,)
    email2 = forms.EmailField()
    class Meta:
        model = BookingsForSafariOpenDates
        fields = ('trip_booked','fi_name', 'la_name', 'email','email2', 'phone_number', 'prefered_destination', 'adults_number', 'children_number','special_request')
        exclude = ['trip_booked']


    def clean(self):
        cleaned_data = super(BookingsForTheSafariCollectionForm, self).clean()
        first_email = cleaned_data.get("email")
        second_email = cleaned_data.get("email2")

        if first_email and second_email:
            # Only do something if both fields are valid so far.
            if first_email != second_email:
                raise forms.ValidationError(
                    "The Two Emails Entered Didn't Match, Try Again"
                )

            return cleaned_data


class BookingsForTheSafariIteneraryForm(forms.ModelForm):
    special_request = forms.CharField(widget = forms.Textarea(), required=True,)
    email2 = forms.EmailField()
    class Meta:
        model = BookingsForIndividualSafariTrip
        fields = ('trip_booked','fi_name', 'la_name', 'email','email2', 'phone_number', 'prefered_destination', 'adults_number', 'children_number','special_request')
        exclude = ['trip_booked']


    def clean(self):
        cleaned_data = super(BookingsForTheSafariIteneraryForm, self).clean()
        first_email = cleaned_data.get("email")
        second_email = cleaned_data.get("email2")

        if first_email and second_email:
            # Only do something if both fields are valid so far.
            if first_email != second_email:
                raise forms.ValidationError(
                    "The Two Emails Entered Didn't Match, Try Again"
                )

            return cleaned_data


class BookingOneDayProgramForm(forms.ModelForm):
    email2 = forms.EmailField()
    special_request = forms.CharField(widget = forms.Textarea(), required=True,)
    class Meta:
        model = BookingsOneDayProgramOpenDate
        fields = ('trip_booked','fi_name', 'la_name', 'email','email2', 'phone_number', 'prefered_destination', 'adults_number', 'children_number','special_request')
        exclude = ['trip_booked']

    def clean(self):
        cleaned_data = super(BookingOneDayProgramForm, self).clean()
        first_email = cleaned_data.get("email")
        second_email = cleaned_data.get("email2")

        if first_email and second_email:
            # Only do something if both fields are valid so far.
            if first_email != second_email:
                raise forms.ValidationError(
                    "The Two Emails Entered Didn't Match, Try Again"
                )

            return cleaned_data

class BookingZanzibarForm(forms.ModelForm):
    email2 = forms.EmailField()
    special_request = forms.CharField(widget = forms.Textarea(), required=True,)
    class Meta:
        model = BookingsForZanzibarOpenDate
        fields = ('trip_booked','fi_name', 'la_name', 'email','email2', 'phone_number', 'prefered_destination', 'adults_number', 'children_number','special_request')
        exclude = ['trip_booked']

    def clean(self):
        cleaned_data = super(BookingZanzibarForm, self).clean()
        first_email = cleaned_data.get("email")
        second_email = cleaned_data.get("email2")

        if first_email and second_email:
            # Only do something if both fields are valid so far.
            if first_email != second_email:
                raise forms.ValidationError(
                    "The Two Emails Entered Didn't Match, Try Again"
                )

            return cleaned_data


class FeedForm(forms.ModelForm):

    feed_body = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Your Message'}), required=True,)
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name'}), required=True,)
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Last Name'}), required=True,)
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder': 'Email Address'}), required=True,)
    nick_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Nick Name'}), required=True,)

    class Meta:
        model=Feed
        fields=('first_name', 'last_name', 'email', 'nick_name', 'feed_body', 'pub_date')
        exclude=['pub_date']

class ContactForm(forms.ModelForm):


    your_message = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Your Message'}), required=True,)
    f_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name'}), required=True,)
    l_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Last Name'}), required=True,)
    email_addr = forms.CharField(widget = forms.EmailInput(attrs={'placeholder': 'Email Address'}), required=True,)
    phone_number = forms.IntegerField(widget = forms.NumberInput(attrs={'placeholder': 'Phone Number'}), required=True,)



    class Meta:
        model=Contact
        fields=('f_name', 'l_name', 'email_addr', 'phone_number', 'your_message', 'time')
        exclude = ['time']
