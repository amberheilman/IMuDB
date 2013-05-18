
from django.conf.urls import patterns, url

from discography import views

urlpatterns = patterns('',
    url(r'^edit/artist/(?P<artist_id>\d+)/$', views.artist_detail, name="edit_artist_detail"),
    url(r'^edit/album/(?P<album_id>\d+)/$', views.album_detail, name="edit_album_detail"),
    url(r'^edit/track/(?P<track_id>\d+)/$', views.track_detail, name="edit_track_detail"),
    url(r'^edit/genre/(?P<genre_id>\d+)/$', views.genre_detail, name="edit_genre_detail"),
    url(r'^edit/credit/(?P<credit_id>\d+)/$', views.credit_detail, name="edit_credit_detail"),
    url(r'^edit/award/(?P<award_id>\d+)/$', views.award_detail, name="edit_award_detail"),
   
    url(r'^add/artist/$', views.artist_add, name="add_artist"),
    url(r'^add/album/$', views.album_add, name="add_album"),
    url(r'^add/track/$', views.track_add, name="add_track"),
    url(r'^add/genre/$', views.genre_add, name="add_genre"),  
    url(r'^add/credit/$', views.credit_add, name="add_credit"),
    url(r'^add/award/$', views.award_add, name="add_award"),    
 
    url(r'^add/thanks/$', views.thanks_add, name="thanks_add"), 
    url(r'^edit/thanks/$', views.thanks, name="thanks"),
   

)
