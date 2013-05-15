from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

COUNTRY_CHOICES = (
    ('USA', 'United States'),
    ('CAN', 'Canada'),
    ('MEX', 'Mexico'),
    ('GBR', 'United Kingdom'),
    ('IND', 'India'),
    ('RUS', 'Russia'),
    ('JPN', 'Japan'),
    ('DEU', 'Germany'),
    ('CHN', 'China'),
)

class Artist(models.Model):
        name = models.CharField(max_length=200)
        country = models.CharField(max_length=3, choices=COUNTRY_CHOICES, null=True, blank=True)
        num_stars = models.IntegerField()
        user = models.ForeignKey(User)

class Genre(models.Model):
        name = models.CharField(max_length=200, null=True)
        style = models.CharField(max_length=2000, null=True, blank=True)
        time_period = models.CharField(max_length=2000, null=True, blank=True)
        origins = models.CharField(max_length=2000, null=True, blank=True)
        critical_reactions = models.CharField(max_length=2000, null=True, blank=True)
        notable_artists = models.ManyToManyField(Artist, null=True, blank=True)
        user = models.ForeignKey(User)

class Album(models.Model):
        title = models.CharField(max_length=200)
        artist = models.ManyToManyField(Artist)
        genre = models.ManyToManyField(Genre, null=True, blank=True)
        production_label = models.CharField(max_length=200, null=True, blank=True)
        explicit = models.BooleanField()
        release_date = models.DateField(null=True, blank=True)
        num_stars = models.IntegerField()
        user = models.ForeignKey(User)
        #will user get overwritten each time an entry is edited? How can I include this behavior in the model?

class Credits(models.Model):
        album = models.OneToOneField(Album)
        exec_producer = models.CharField(max_length=200, null=True, blank=True)
        mastered_by = models.CharField(max_length=200, null=True, blank=True)
        marketing = models.CharField(max_length=200, null=True, blank=True)
        creative_director = models.CharField(max_length=200, null=True, blank=True)
        art_director = models.CharField(max_length=200, null=True, blank=True)
        photography = models.CharField(max_length=200, null=True, blank=True)
        user = models.ForeignKey(User)

class AwardOrg(models.Model):
	name = models.CharField(max_length=200)

class AwardCategory(models.Model):
	name = models.CharField(max_length=200)
	awardorg = models.ForeignKey(AwardOrg)
	year = models.IntegerField()

class Track(models.Model):
	title = models.CharField(max_length=200)
	album = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist)
	length = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	release_date = models.DateField(null=True, blank=True)
	num_stars = models.IntegerField()
	user = models.ForeignKey(User)


class Award(models.Model):
	album = models.ForeignKey(Album, null=True, blank=True)
	track = models.ForeignKey(Track, null=True, blank=True)
	artist = models.ForeignKey(Artist)
	awardcategory = models.OneToOneField(AwardCategory)
        user = models.ForeignKey(User)

class ArtistForm(ModelForm):
        class Meta:
                model = Artist
 
class GenreForm(ModelForm):
        class Meta:
                model = Genre
 
class AlbumForm(ModelForm):
        class Meta:
                model = Album
                
class CreditsForm(ModelForm):
        class Meta:
                model = Credits
          
class TrackForm(ModelForm):
        class Meta:
                model = Track

class AwardForm(ModelForm):
	class Meta:
		model = Award
