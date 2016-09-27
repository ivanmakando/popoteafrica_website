from django.template import *
from django.contrib.auth import *
from django.http import *
from django.contrib.auth.models import *
#from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
#from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
#from django.contrib.auth import login as django_login, authenticate
#from django.utils import timezone
#from random import sample
from django.shortcuts import *
from django.utils import timezone
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect
from popoteafrica.models import *
from popoteafrica.forms import *
from django.utils import timezone

def ThankYouPage(request):
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    returning  = RequestContext(request, {
        'feeds':feeds,
        'partners':partners
    })
    return render_to_response('thank_you.html', returning)


def SafariItenerary(request):

    activity = ItenearyForSafari.objects.all()
    route = Route.objects.get(id = 50)
    feeds = Feed.objects.all().order_by('-pub_date')
    variables = RequestContext(request, {
        'activity':activity,
        'route':route,
        'feeds':feeds,
        'route':route
    })
    return render_to_response('safari-iteneary.html', variables)


def AllOneDayObjects(request):
    route = Route.objects.get(id = 54)
    trip = AllOneDayProgramTripsForOpenDates.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    values = RequestContext(request, {
        'trip':trip,
        'feeds':feeds,
        'route':route,
        'partners':partners
    })
    return render_to_response('all_one_day_plans.html', values)

@csrf_protect
def OneDayplansBooking(request, id):
    route = Route.objects.get(id = 7)
    feeds = Feed.objects.all().order_by('-pub_date')
    the_trip = AllOneDayProgramTripsForOpenDates.objects.get(id = id)
    partners = Partners.objects.get(id = 2)
    if request.method == 'POST':
        form = BookingOneDayProgramForm(request.POST)
        if form.is_valid():
            safari = form.save(commit = False)
            safari.trip_booked = the_trip
            safari.fi_name = request.POST.get('fi_name')
            safari.la_name = request.POST.get('la_name')
            safari.email = request.POST.get('email')
            safari.phone_number = request.POST.get('phone_number')
            safari.prefered_destination = request.POST.get('prefered_destination')
            safari.adults_number = request.POST.get('adults_number')
            safari.children_number = request.POST.get('children_number')
            safari.special_request = request.POST.get('special_request')
            safari.save()

            return HttpResponseRedirect('/thank_you')
    else:
        form = BookingOneDayProgramForm()
    return render(request, 'oneday-bookings.html', {'feeds':feeds, 'form':form,'route':route, 'the_trip':the_trip, 'partners':partners})

def AllZanzibarObjects(request):
    route = Route.objects.get(id = 54)
    trip = AllZanzibarTripsForOpenDates.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    values = RequestContext(request, {
        'trip':trip,
        'feeds':feeds,
        'route':route,
        'partners':partners
    })
    return render_to_response('all_zanzibar_plans.html', values)

@csrf_protect
def ZanzibarplansBooking(request, id):
    partners = Partners.objects.get(id = 2)
    route = Route.objects.get(id = 7)
    feeds = Feed.objects.all().order_by('-pub_date')
    the_trip = AllZanzibarTripsForOpenDates.objects.get(id = id)
    if request.method == 'POST':
        form = BookingZanzibarForm(request.POST)
        if form.is_valid():
            safari = form.save(commit = False)
            safari.trip_booked = the_trip
            safari.fi_name = request.POST.get('fi_name')
            safari.la_name = request.POST.get('la_name')
            safari.email = request.POST.get('email')
            safari.phone_number = request.POST.get('phone_number')
            safari.prefered_destination = request.POST.get('prefered_destination')
            safari.adults_number = request.POST.get('adults_number')
            safari.children_number = request.POST.get('children_number')
            safari.special_request = request.POST.get('special_request')
            safari.save()

            return HttpResponseRedirect('/thank_you')
    else:
        form = BookingZanzibarForm()
    return render(request, 'zanzibar-bookings.html', {'feeds':feeds, 'form':form,'route':route, 'the_trip':the_trip, 'partners':partners})


def AllMountainObjects(request):
    route = Route.objects.get(id = 54)
    trip = AllMountainTripsForOpenDates.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    values = RequestContext(request, {
        'trip':trip,
        'feeds':feeds,
        'route':route,
        'partners':partners
    })
    return render_to_response('all_mountain_plans.html', values)

@csrf_protect
def MountainplansBooking(request, id):
    route = Route.objects.get(id = 7)
    feeds = Feed.objects.all().order_by('-pub_date')
    the_trip = AllMountainTripsForOpenDates.objects.get(id = id)
    if request.method == 'POST':
        form = BookingAMountainForm(request.POST)
        if form.is_valid():
            safari = form.save(commit = False)
            safari.trip_booked = the_trip
            safari.fi_name = request.POST.get('fi_name')
            safari.la_name = request.POST.get('la_name')
            safari.email = request.POST.get('email')
            safari.phone_number = request.POST.get('phone_number')
            safari.prefered_destination = request.POST.get('prefered_destination')
            safari.adults_number = request.POST.get('adults_number')
            safari.children_number = request.POST.get('children_number')
            safari.special_request = request.POST.get('special_request')
            safari.save()

            return HttpResponseRedirect('/thank_you')
    else:
        form = BookingAMountainForm()
    return render(request, 'mountain-bookings.html', {'feeds':feeds, 'form':form,'route':route, 'the_trip':the_trip})

def AllSafariObjects(request):
    route = Route.objects.get(id = 54)
    trip = AllSafariTripsForOpenDates.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    values = RequestContext(request, {
        'trip':trip,
        'feeds':feeds,
        'route':route,
        'partners':partners
    })
    return render_to_response('all_safari_plans.html', values)

@csrf_protect
def SafariplansBooking(request, id):
    route = Route.objects.get(id = 7)
    feeds = Feed.objects.all().order_by('-pub_date')
    thetrip = AllSafariTripsForOpenDates.objects.get(id = id)
    partners = Partners.objects.get(id = 2)
    if request.method == 'POST':
        form = BookingsForTheSafariCollectionForm(request.POST)
        if form.is_valid():
            safaritrip = form.save(commit = False)
            safaritrip.trip_booked = thetrip
            safaritrip.fi_name = request.POST.get('fi_name')
            safaritrip.la_name = request.POST.get('la_name')
            safaritrip.email = request.POST.get('email')
            safaritrip.phone_number = request.POST.get('phone_number')
            safaritrip.prefered_destination = request.POST.get('prefered_destination')
            safaritrip.adults_number = request.POST.get('adults_number')
            safaritrip.children_number = request.POST.get('children_number')
            safaritrip.special_request = request.POST.get('special_request')
            safaritrip.save()

            return HttpResponseRedirect('/thank_you')
    else:
        form = BookingsForTheSafariCollectionForm()
    return render(request, 'safari-trip-bookings.html', {'feeds':feeds, 'form':form,'route':route, 'the_trip':thetrip, 'partners':partners})

@csrf_protect
def SafariIteneraryplansBooking(request, id):
    route = Route.objects.get(id = 7)
    feeds = Feed.objects.all().order_by('-pub_date')
    the_itienary = SafariPlansForTheChart.objects.get(id = id)
    partners = Partners.objects.get(id = 2)
    if request.method == 'POST':
        form = BookingsForTheSafariIteneraryForm(request.POST)
        if form.is_valid():
            safaritrip = form.save(commit = False)
            safaritrip.trip_booked = the_itienary
            safaritrip.fi_name = request.POST.get('fi_name')
            safaritrip.la_name = request.POST.get('la_name')
            safaritrip.email = request.POST.get('email')
            safaritrip.phone_number = request.POST.get('phone_number')
            safaritrip.prefered_destination = request.POST.get('prefered_destination')
            safaritrip.adults_number = request.POST.get('adults_number')
            safaritrip.children_number = request.POST.get('children_number')
            safaritrip.special_request = request.POST.get('special_request')
            safaritrip.save()

            return HttpResponseRedirect('/thank_you')
    else:
        form = BookingsForTheSafariIteneraryForm()
    return render(request, 'safari-object-bookings.html', {'feeds':feeds, 'form':form,'route':route, 'the_itienary':the_itienary, 'partners':partners})




def ClimbKilimanjaroTipsView(request):
    route = Route.objects.get(id = 53)
    plan = ClimbKilimanjaroTips.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'plan':plan,
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('climbing_kilimanjaro_tips.html', content)

def SafariPackListView(request):
    packages = SafariPackList.objects.all()
    route = Route.objects.get(id = 49)
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'feeds':feeds,
        'route':route,
        'packages': packages,
    })

    return render_to_response('safari_packlist.html', content)

def KilimanjaroPackList(request):
    packages = KiliPackList.objects.all()
    route = Route.objects.get(id = 48)
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'feeds':feeds,
        'route':route,
        'packages': packages,
    })

    return render_to_response('kilimanjaro_packlist.html', content)

def WhenToClimb(request):
    route = Route.objects.get(id = 51)
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('when_to_climb.html', content)

def AboutTanzania(request):
    route = Route.objects.get(id = 47)
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('about_tanzania.html', content)

def AnimalMigrationsView(request):
    route = Route.objects.get(id = 52)
    plan = AnimalMigrations.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'plan':plan,
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('animal_migration.html', content)

def PlanASafariView(request):
    route = Route.objects.get(id = 50)
    plan = HowToPlanASafari.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'plan':plan,
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('plan_a_safari.html', content)


def FAQView(request):
    route = Route.objects.get(id = 46)
    faq = FAQ.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'faq':faq,
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('faqs_page.html', content)

def TermsAndConditionsView(request):
    route = Route.objects.get(id = 55)
    terms = TermsAndConditions.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'terms':terms,
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('terms-and-conditions.html', content)

def AboutGuidesView(request):
    route = Route.objects.get(id = 56)
    about = AboutGuides.objects.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    content = RequestContext(request, {
        'about':about,
        'feeds':feeds,
        'route':route,
    })

    return render_to_response('about-guides.html', content)


@csrf_protect
def IndividualBooking(request):
    route = Route.objects.get(id = 7)
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    if request.method == 'POST':
        form = BookingIndividualForm(request.POST)
        if form.is_valid():
            booking = form.save(commit = False)
            booking.fir_name = request.POST.get('fir_name')
            booking.las_name = request.POST.get('las_name')
            booking.email_add = request.POST.get('email_add')
            booking.phone_no = request.POST.get('phone_no')
            booking.pref_destination = request.POST.get('pref_destination')
            booking.adults_no = request.POST.get('adults_no')
            booking.children_no = request.POST.get('children_no')
            booking.special_requests = request.POST.get('special_requests')
            booking.save()

            return HttpResponseRedirect('/thank_you')
    else:
        form = BookingIndividualForm()

    return render(request, 'booking.html',{'form':form, 'route':route, 'feeds':feeds, 'partners':partners},)


def Homepage(request):
    message = "the templates work"
    team = OurTeam.objects.get(id = 1)
    value = timezone.now()
    partners = Partners.objects.get(id = 2)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    content = MainPageContent.objects.get(id = 1)
    gallery = Gallery.objects.get(id = 5)
    feeds = Feed.objects.all().order_by('-pub_date')
    time = timezone.now()
    outputmesage = RequestContext(request,{
        'content':content,
        'time':time,
        'gallery': gallery,
        'feeds':feeds,
        'request':request,
        'team':team,
        'gen_gallery': gen_gallery,
        'partners': partners
                    })
    return render_to_response("index.html",outputmesage)

def iframe(request):
    return render_to_response('test.html', {'request':request})

def ProductDetails(request):
    route = Route.objects.get(id = 21)
    info = SafariPlansForTheChart.objects.all()
    info2 = route.tripsevendayinfo_set.all()
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 1)
    containing = RequestContext(request,{
        'info':info,
        'info2': info2,
        'feeds': feeds,
        'partners': partners,
    })
    return render_to_response('lemosho.html',containing,request)


def AdventuresList(request):
    return render_to_response('shop-grid-no-sidebar.html', request)

def ShopList(request):
    return render_to_response('shop-list.html', request)

def SignIn(request):
    return render_to_response('signin.html', request)


def AboutUs(request):
    team = OurTeam.objects.get(id = 1)
    route = Route.objects.get(id = 5)
    feeds = Feed.objects.all().order_by('-pub_date')
    partners = Partners.objects.get(id = 2)
    values = RequestContext(request,{
        'feeds':feeds,
        'partners':partners,
        'team': team,
        'route':route,

    })
    return render_to_response('about.html', values)

def Serengeti(request):
    trip = SafariPlansForTheChart.objects.all()
    activity = Activities.objects.get(id = 1)
    info = SafariPlansForTheChart.objects.all()
    route = Route.objects.get(id = 9)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 4)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'info':info,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'trip':trip
    })
    return render_to_response('navbar/safari/northern/serengeti.html', values)

def LemoshoRoute(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 4)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 15)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'info':info,
        'info2': info2,
    })
    return render_to_response('navbar/mountain/lemosho.html', values)

def LemoshoRoute_2(request):
    activity = Activities.objects.get(id = 9)
    route = Route.objects.get(id = 4)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 15)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'info':info,
        'info2': info2,
    })
    return render_to_response('navbar/mountain/lemosho_2.html', values)


def MachameRoute(request):
    activity = Activities.objects.get(id = 4)
    route = Route.objects.get(id = 20)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 16)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'info':info,
        'info2': info2,
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/machame.html', values)

def MachameRoute_2(request):
    activity = Activities.objects.get(id = 12)
    route = Route.objects.get(id = 20)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 16)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'info':info,
        'info2': info2,
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/machame_2.html', values)



def MaranguRoute(request):
    activity = Activities.objects.get(id = 2)
    route = Route.objects.get(id = 21)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 17)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'info':info,
        'info2': info2,
    })
    return render_to_response('navbar/mountain/marangu.html', values)

def MaranguRoute_2(request):
    activity = Activities.objects.get(id = 10)
    route = Route.objects.get(id = 21)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 17)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'info':info,
        'info2': info2,
    })
    return render_to_response('navbar/mountain/marangu_2.html', values)



def RongaiRoute(request):
    activity = Activities.objects.get(id = 5)
    route = Route.objects.get(id = 22)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 18)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'info':info,
        'info2': info2,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/rongai.html', values)

def RongaiRoute_2(request):
    activity = Activities.objects.get(id = 13)
    route = Route.objects.get(id = 22)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 18)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'info':info,
        'info2': info2,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/rongai_2.html', values)

def MwekaRoute(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 23)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 19)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/mweka.html', values)


def ShiraRoute(request):
    activity = Activities.objects.get(id = 11)
    route = Route.objects.get(id = 24)
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 20)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'info':info,
        'info2': info2,
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/shira.html', values)

def ShiraRoute_2(request):
    activity = Activities.objects.get(id = 3)
    route = Route.objects.get(id = 24)
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 20)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'info':info,
        'info2': info2,
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/shira_2.html', values)

def UmbweRoute(request):
    activity = Activities.objects.get(id = 6)
    route = Route.objects.get(id = 25)
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 2)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'info':info,
        'info2': info2,
    })
    return render_to_response('navbar/mountain/umbwe.html', values)

def UmbweRoute_2(request):
    activity = Activities.objects.get(id = 14)
    route = Route.objects.get(id = 25)
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 2)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery,
        'info':info,
        'info2': info2,
    })
    return render_to_response('navbar/mountain/umbwe_2.html', values)

def Meru(request):
    activity = Activities.objects.get(id = 8)
    route = Route.objects.get(id = 26)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 21)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = route.tripsixdayinfo_set.all()
    info2 = route.tripsevendayinfo_set.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'info':info,
        'info2':info2,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/other/meru.html', values)

def OlDoinyoLengai(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 27)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 22)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/mountain/other/ol-doinyo-lengai.html', values)

def OlduvaiGorge(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 10)
    info = SafariPlansForTheChart.objects.all()
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 5)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'info':info,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/northern/olduvai-gorge.html', values)

def NgorongoroCrater(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 11)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 6)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    info = SafariPlansForTheChart.objects.all()
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'info':info,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/northern/ngorongoro-crater.html', values)


def ManyaraNationalPark(request):
    info = SafariPlansForTheChart.objects.all()
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 12)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 7)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'info':info,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/northern/manyara-national-park.html', values)


def Tarangire(request):
    activity = Activities.objects.get(id = 1)
    info = SafariPlansForTheChart.objects.all()
    route = Route.objects.get(id = 13)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 8)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'info':info,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/northern/tarangire-national-park.html', values)


def WildebeestMigration(request):
    activity = Activities.objects.get(id = 1)
    info = SafariPlansForTheChart.objects.all()
    route = Route.objects.get(id = 14)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 9)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'info':info,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/northern/the-great-wildebeest-migration.html', values)

def Mikumi(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 15)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 10)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/southern/mikumi-national-park.html', values)

def Ruaha(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 16)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 11)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/southern/ruaha-national-park.html', values)

def Selous(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 17)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 12)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/southern/selous-game-eserve.html', values)

def Tanganyika(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 18)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 13)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/western/lake-tanganyika.html', values)

def Gombe(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 19)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 14)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/safari/western/gombe-stream-national-park.html', values)

def SunshineHotel(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 28)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 23)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/lodges/sunshine-hotel-nungwe.html', values)

def JaferyHouse(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 29)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 24)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/lodges/jafery-house-spa-stone-town.html', values)

def ZenjiHotel(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 32)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 25)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/lodges/zenji-hotel-stone-town.html', values)

def LemonHouse(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 30)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 37)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/lodges/lemon-house-stone-town.html', values)

def DiamondMapenzi(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 31)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 26)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/lodges/diamond-mapenzi-kiwengwe.html', values)

def StoneTown(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 33)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 27)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/evening-walk-in-stone-town.html', values)

def DhowCruise(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 34)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 28)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/sundown-dhow-cruise.html', values)

def SpiceTour(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 35)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 29)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/zanzibar-spice-tour.html', values)

def JohaniForest(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 36)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 30)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/the-johani-forest.html', values)

def StoneTownTour(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 37)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 31)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/stone-town-tour.html', values)

def PrisonIsland(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 38)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 32)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/prison-island.html', values)

def TheDolphin(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 39)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 3)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/zanzibar/tours/the-dolphin.html', values)

def LakeChala(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 40)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 33)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/one_day/lake-chala.html', values)

def MandaraHut(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 41)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 34)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/one_day/mandara-hut.html', values)

def MateruniWaterfalls(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 42)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 35)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/one_day/materuni-waterfalls.html', values)

def MaranguWaterfalls(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 43)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 36)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/one_day/marangu-waterfalls.html', values)

def KikuletwaHotSprings(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 44)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 39)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/one_day/kikuletwa-hot-springs.html', values)

def OlpopongiMasaiMuseum(request):
    activity = Activities.objects.get(id = 1)
    route = Route.objects.get(id = 45)
    gen_gallery = GeneralGallery.objects.get(id=  1)
    trip_gallery  = TripGallery.objects.get(id = 38)
    best_selling = BestSellingTrips.objects.get(id = 1)
    feeds = Feed.objects.all().order_by('-pub_date')
    values = RequestContext(request, {
        'feeds':feeds,
        'trip_gallery': trip_gallery,
        'best_selling': best_selling,
        'activity':activity,
        'route': route,
        'gen_gallery': gen_gallery
    })
    return render_to_response('navbar/one_day/Olpopongi-masai-museum.html', values)

@csrf_protect
def FeedViews(request):
    partners = Partners.objects.get(id = 1)
    route = Route.objects.get(id = 8)
    feeds = Feed.objects.all().order_by('-pub_date')
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.pub_date = request.POST.get('pub_date')
            feed.feed_body = request.POST.get('feed_body')
            feed.first_name = request.POST.get('first_name')
            feed.last_name = request.POST.get('last_name')
            feed.email = request.POST.get('email')
            feed.nick_name = request.POST.get('nick_name')
            feed.save()
            return HttpResponseRedirect('/home')
    else:
        form = FeedForm()

    return render(request, 'feeds.html', {'form':form, 'feeds':feeds, 'route':route, 'partners':partners}, )

@csrf_protect
def ContactUs(request):
    route = Route.objects.get(id = 6)
    partners = Partners.objects.get(id = 2)
    feeds = Feed.objects.all().order_by('-pub_date')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
#            contact.f_name=request.POST.get('f_name')
#            contact.l_name=request.POST.get('l_name')
#            contact.email_addr=request.POST.get('email_addr')
            contact.phone_number=request.POST.get('phone_number')
#            contact.your_message=request.POST.get('your_message')
#            contact.time=request.POST.get('time')
            form.save()

            return HttpResponseRedirect('/home')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form':form, 'feeds':feeds, 'partners':partners, 'route':route}, )
