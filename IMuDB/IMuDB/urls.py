from django.conf.urls.defaults import *
from IMuDB.views import HomePageView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IMuDB.views.home', name='home'),
    # url(r'^IMuDB/', include('IMuDB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^accounts/', include('registration.backends.default.urls')),
      url(r'^discography/', include('discography.urls')),
      url(r'^$', HomePageView.as_view(), name='home'),
)
