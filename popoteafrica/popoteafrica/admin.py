from django.contrib import admin
from popoteafrica.models import *


class BookingIndividualAdmin(admin.ModelAdmin):
    fields = ['fir_name', 'las_name', 'email_add', 'phone_no', 'pref_destination', 'adults_no', 'children_no', 'special_requests']
    readonly_fields = ['fir_name', 'las_name', 'email_add', 'phone_no', 'pref_destination', 'adults_no', 'children_no', 'special_requests']


admin.site.register(BookingsForIndividualTrip,BookingIndividualAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    fields = ['f_name', 'l_name', 'email_addr', 'phone_number', 'your_message', 'time']
    readonly_fields = ['f_name', 'l_name', 'email_addr', 'phone_number', 'your_message', 'time']

admin.site.register(Contact, ContactUsAdmin)

class BookingsForOneDayProgramAdmin(admin.ModelAdmin):
    fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']
    readonly_fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']

admin.site.register(BookingsOneDayProgramOpenDate,BookingsForOneDayProgramAdmin)

class BookingsForZanzibarAdmin(admin.ModelAdmin):
    fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']
    readonly_fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']

admin.site.register(BookingsForZanzibarOpenDate,BookingsForZanzibarAdmin)

class BookingsForAMountainAdmin(admin.ModelAdmin):
    fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']
    readonly_fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']

admin.site.register(BookingsMountainOpenDates, BookingsForAMountainAdmin)

class BookingsForTheSafariCollectionAdmin(admin.ModelAdmin):
    fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']
    readonly_fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']

admin.site.register(BookingsForSafariOpenDates, BookingsForTheSafariCollectionAdmin)



class BookingsForTheSafariItenearyAdmin(admin.ModelAdmin):
    fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']
    readonly_fields = ['fi_name', 'la_name', 'email', 'phone_number', 'prefered_destination', 'adults_number', 'children_number', 'special_request', 'trip_booked']

admin.site.register(BookingsForIndividualSafariTrip, BookingsForTheSafariItenearyAdmin)



admin.site.register(MainPageContent)
admin.site.register(Gallery)
admin.site.register(Feed)
admin.site.register(GeneralGallery)
admin.site.register(Activities)
admin.site.register(OurTeam)
admin.site.register(Route)
admin.site.register(TripGallery)
admin.site.register(BestSellingTrips)
admin.site.register(Partners)
admin.site.register(TripSixDayInfo)
admin.site.register(TripSevenDayInfo)
admin.site.register(FAQ)
admin.site.register(KiliPackList)
admin.site.register(SafariPackList)
admin.site.register(HowToPlanASafari)
admin.site.register(AnimalMigrations)
admin.site.register(ClimbKilimanjaroTips)
admin.site.register(AllMountainTripsForOpenDates)
admin.site.register(AllOneDayProgramTripsForOpenDates)
admin.site.register(AllZanzibarTripsForOpenDates)
admin.site.register(SafariPlansForTheChart)
admin.site.register(ItenearyForSafari)
admin.site.register(AllSafariTripsForOpenDates)
admin.site.register(TermsAndConditions)
admin.site.register(AboutGuides)
