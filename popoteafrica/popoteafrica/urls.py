"""popoteafrica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os.path
from django.conf import *
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import *
from popoteafrica.views import AllSafariObjects,SafariIteneraryplansBooking,TermsAndConditionsView, AboutGuidesView, SafariplansBooking,Homepage,SafariItenerary,ThankYouPage,AllMountainObjects,AllOneDayObjects, OneDayplansBooking,MountainplansBooking,AllZanzibarObjects,ZanzibarplansBooking, ProductDetails,iframe,ClimbKilimanjaroTips, ClimbKilimanjaroTipsView, KilimanjaroPackList,SafariPackListView,PlanASafariView,WhenToClimb,AnimalMigrationsView, FAQView,AboutTanzania, ShopList, ContactUs,IndividualBooking, SignIn, AdventuresList, AboutUs,ShiraRoute,ShiraRoute_2, Meru, OlDoinyoLengai, UmbweRoute,UmbweRoute_2, MwekaRoute, LemoshoRoute,LemoshoRoute_2, FeedViews, MachameRoute,MachameRoute_2, MaranguRoute,MaranguRoute_2,RongaiRoute,RongaiRoute_2, Serengeti,ManyaraNationalPark, OlduvaiGorge, NgorongoroCrater, Tarangire, WildebeestMigration, Mikumi, Ruaha, Selous, Tanganyika, Gombe, SunshineHotel, JaferyHouse, ZenjiHotel, LemonHouse, DiamondMapenzi, StoneTown, DhowCruise, SpiceTour, JohaniForest, StoneTownTour, PrisonIsland, TheDolphin, LakeChala, MandaraHut, MateruniWaterfalls, MaranguWaterfalls, KikuletwaHotSprings, OlpopongiMasaiMuseum
"Rename the links they are mistakenly arranged"


admin.autodiscover()


site_media=os.path.join(
    os.path.dirname(__file__), 'site_media'

)

admin.site.site_header = ('Popoteafrica Admin')
admin.site.index_title = ('Contents Area')
admin.site.site_title = ('Popoteafrica adminsitration Area')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^support/', include('live_support.urls')),
    url(regex=r'^home/$', view = Homepage, name= 'home_page'),
    url(regex=r'^iframe/', view = iframe, name= 'iframe' ),
    url(regex=r'^products/$', view = ProductDetails, name= 'product_details'),
    url(regex=r'^adventures/$', view = AdventuresList, name= 'adventures-list'),
    url(regex=r'^shoplist/$', view = ShopList, name= 'shop-list'),
    url(regex=r'^signin/$', view = SignIn, name= 'sign-in'),
    url(regex=r'^register/$', view = SignIn, name= 'sign-in'),
    url(regex=r'^contactus/$', view = ContactUs, name= 'contact-us'),
    url(regex=r'^about/$', view = AboutUs, name= 'about-us'),
    url(regex=r'^feeds/$', view = FeedViews, name= 'feeds'),
    url(regex=r'^booking/$', view = IndividualBooking, name= 'booking-individual'),
    url(regex=r'^faq/$', view = FAQView, name= 'FAQ-view'),
    url(regex=r'^about_tanzania/$', view = AboutTanzania, name= 'about-tanzania'),
    url(regex=r'^kilimanjaro-pack-list/$', view = KilimanjaroPackList, name= 'kilimanjaro-pack-list'),
    url(regex=r'^tanzania-safari-pack-list/$', view = SafariPackListView, name= 'safari-packList'),
    url(regex=r'^how-to-plan-your-safari/$', view = PlanASafariView, name= 'plan-a-safari'),
    url(regex=r'^best-kilimanjaro-climbing-time/$', view = WhenToClimb, name= 'when-to-climb'),
    url(regex=r'^animal-migrations/$', view = AnimalMigrationsView, name= 'animal-migrations'),
    url(regex=r'^tips-kilimanjaro-climbs/$', view = ClimbKilimanjaroTipsView, name= 'climb-kilimanjaro-tips'),
    url(regex=r'^kilimanjaro-all-plans/$', view = AllMountainObjects, name= 'kilimanjaro-all-plans'),
    url(regex=r'^booking_mountain/(?P<id>\d+)$', view = MountainplansBooking, name= 'safari-plans-booking'),
    url(regex=r'^zanzibar-all-plans/$', view = AllZanzibarObjects, name= 'zanzibar-all-plans'),
    url(regex=r'^booking_zanzibar/(?P<id>\d+)$', view = ZanzibarplansBooking, name= 'zanzibar-plans-booking'),
    url(regex=r'^one-day-all-plans/$', view = AllOneDayObjects, name= 'oneday-all-plans'),
    url(regex=r'^booking_one_day/(?P<id>\d+)$', view = OneDayplansBooking, name= 'oneday-plans-booking'),
    url(regex=r'^booking_trip/(?P<id>\d+)$', view = SafariIteneraryplansBooking, name= 'Safari-itenerary-plans-booking'),
    url(regex=r'^safari-itinerary/$', view = SafariItenerary, name= 'safari-itenerary'),
    url(regex=r'^thank_you/$', view = ThankYouPage, name= 'thank-you-page'),
    url(regex=r'^safari-all-plans/$', view = AllSafariObjects, name= 'oneday-all-plans'),
    url(regex=r'^booking_safari/(?P<id>\d+)$', view = SafariplansBooking, name= 'oneday-plans-booking'),
    url(regex=r'^terms_and_conditions/$', view = TermsAndConditionsView, name= 'terms-and-conditions'),
    url(regex=r'^our-guides-potters/$', view = AboutGuidesView, name= 'about-guides'),

#Mountain Routes
    url(regex=r'^lemosho-seven-days/$', view = LemoshoRoute, name= ' lemosho-route'),
    url(regex=r'^lemosho-eight-days/$', view = LemoshoRoute_2, name= ' lemosho-route_2'),
    url(regex=r'^machame-six-days/$', view = MachameRoute, name= ' machame-route'),
    url(regex=r'^machame-seven-days/$', view = MachameRoute_2, name= ' machame-route_2'),
    url(regex=r'^marangu-five-days/$', view = MaranguRoute, name= ' marangu-route'),
    url(regex=r'^marangu-six-days/$', view = MaranguRoute_2, name= ' marangu-route_2'),
    url(regex=r'^rongai-six-days/$', view = RongaiRoute, name= ' rongai-route'),
    url(regex=r'^rongai-seven-days/$', view = RongaiRoute_2, name= ' rongai-route_2'),
    url(regex=r'^mweka/$', view = MwekaRoute, name= ' mweka-route'),
    url(regex=r'^northern-circuit-eight-days/$', view = ShiraRoute, name= ' shira-route'),
    url(regex=r'^northern-circuit-nine-days/$', view = ShiraRoute_2, name= ' shira-route_2'),
    url(regex=r'^umbwe-six-days/$', view = UmbweRoute, name= ' umbwe-route'),
    url(regex=r'^umbwe-seven-days/$', view = UmbweRoute_2, name= ' umbwe-route'),
    url(regex=r'^meru/$', view = Meru, name= 'Meru'),
    url(regex=r'^ol-doinyo-lengai/$', view = OlDoinyoLengai, name= 'OlDoinyoLengai'),
#safari
    url(regex=r'^serengeti/$', view = Serengeti, name= 'serengeti'),
    url(regex=r'^olduvai-gorge/$', view = OlduvaiGorge, name= 'Olduvai-Gorge'),
    url(regex=r'^ngorongoro-crater/$', view = NgorongoroCrater, name= 'ngorongoro-crater'),
    url(regex=r'^manyara-national-park/$', view = ManyaraNationalPark, name= 'manyara-national-park'),
    url(regex=r'^tarangire-national-park/$', view = Tarangire, name= 'tarangire-national-park'),
    url(regex=r'^the-great-wildebeest-migration/$', view = WildebeestMigration, name= 'the-great-wildebeest-migration'),
    url(regex=r'^mikumi-national-park/$', view = Mikumi, name= 'mikumi-national-park'),
    url(regex=r'^ruaha-national-park/$', view = Ruaha, name= 'ruaha-national-park'),
    url(regex=r'^selous-game-eserve/$', view = Selous, name= 'selous-game-eserve'),
    url(regex=r'^lake-tanganyika/$', view = Tanganyika, name= 'lake-tanganyika'),
    url(regex=r'^gombe-stream-national-park/$', view = Gombe, name= 'gombe-stream-national-park'),
#ZANZIBAR
    url(regex=r'^sunshine-hotel-nungwe/$', view = SunshineHotel, name= 'sunshine-hotel-nungwe'),
    url(regex=r'^jafery-house-spa-stone-town/$', view = JaferyHouse, name= 'jafery-house-spa-stone-town'),
    url(regex=r'^zenji-hotel-stone-town/$', view = ZenjiHotel, name= 'zenji-hotel-stone-town'),
    url(regex=r'^lemon-house-stone-town/$', view = LemonHouse, name= 'lemon-house-stone-town'),
    url(regex=r'^diamond-mapenzi-kiwengwe/$', view = DiamondMapenzi, name= 'diamond-mapenzi-kiwengwe'),
    url(regex=r'^evening-walk-in-stone-town/$', view = StoneTown, name= 'evening-walk-in-stone-town'),
    url(regex=r'^sundown-dhow-cruise/$', view = DhowCruise, name= 'sundown-dhow-cruise'),
    url(regex=r'^zanzibar-spice-tour/$', view = SpiceTour, name= 'zanzibar-spice-tour'),
    url(regex=r'^the-jozani-forest/$', view = JohaniForest, name= 'the-johani-forest'),
    url(regex=r'^stone-town-tour/$', view = StoneTownTour, name= 'stone-town-tour'),
    url(regex=r'^prison-island/$', view = PrisonIsland, name= 'prison-island'),
    url(regex=r'^the-dolphin/$', view = TheDolphin, name= 'the-dolphin'),
    url(regex=r'^lake-chala/$', view = LakeChala, name= 'lake-chala'),
    url(regex=r'^mandara-hut/$', view = MandaraHut, name= 'mandara-hut'),
    url(regex=r'^materuni-waterfalls/$', view = MateruniWaterfalls, name= 'materuni-waterfalls'),
    url(regex=r'^marangu-waterfalls/$', view = MaranguWaterfalls, name= 'marangu-waterfalls'),
    url(regex=r'^kikuletwa-hot-springs/$', view = KikuletwaHotSprings, name= 'kikuletwa-hot-springs'),
    url(regex=r'^Olpopongi-masai-museum/$', view = OlpopongiMasaiMuseum, name= 'Olpopongi-masai-museum'),

    url('^cropper/', include('cropper.urls')),
    url('^', include('live_support.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
