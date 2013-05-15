
from django.contrib import admin
from discography.models import Artist, Album, Genre, Track, AwardOrg, AwardCategory, Award, Credit

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(AwardOrg)
admin.site.register(AwardCategory)
admin.site.register(Award)
admin.site.register(Credit)
