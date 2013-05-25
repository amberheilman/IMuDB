"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
<<<<<<< HEAD
from django.test.client import Client
from django.core.urlresolvers import reverse
from discography.models import Artist, Album, Genre
from django.contrib.auth.models import User

def create_artist(name, country, num_stars):
    
    return Artist.objects.create(name=name, country=country, num_stars=num_stars)

class ArtistViewTests(TestCase):

	def setUp(self):
	
		user = User.objects.create_user(username="stephen", password="password")
		user.is_active = True
		user.is_staff = True
		user.save()
		self.assertEqual(User.objects.all().count(), 1)
	
	def test_artist_detail_view_GET_request(self):

		self.assertTrue(self.client.login(username='stephen', password='password'))
        	artist = create_artist(name="Lionel Ritchie", country="USA", num_stars=5)
		response = self.client.get(reverse("edit_artist_detail", args=(artist.id,)))
		for template in response.templates:
			self.assertEqual(template.name, 'edit.html')
		self.assertContains(response, 'form')
        
	def test_artist_detail_view_POST_request(self):
		
		self.assertTrue(self.client.login(username='stephen', password='password'))
		artist = create_artist(name="Lionel Ritchie", country="USA", num_stars=5)

		response = self.client.post(reverse("edit_artist_detail", args=(artist.id,)), data={'name': 'Stephen Slaughter', 'country': 'USA', 'num_stars': 5})
		for template in response.templates:
			self.assertEqual(template.name, 'thanks.html')

	def test_artist_add_view_POST_request(self):
	
		self.assertTrue(self.client.login(username='stephen', password='password'))
		artist = create_artist(name="Lionel Ritchie", country="USA", num_stars=5)
		response = self.client.post(reverse("add_artist"), data={'name': 'Stephen Slaughter', 'country':'USA', 'num_stars':5})
		for template in response.templates:
			self.assertEqual(template.name, 'thanksadd.html')

	def test_artist_add_view_GET_request(self):
		
		self.assertTrue(self.client.login(username='stephen', password='password'))
                artist = create_artist(name="Lionel Ritchie", country="USA", num_stars=5)
                response = self.client.get(reverse("add_artist"))
                for template in response.templates:
                        self.assertEqual(template.name, 'add.html')

	#def test_artist_search_view_GET_request(self):

	
def create_album(title, production_label, explicit, release_date, num_stars):
	       album = Album.objects.create(title=title, production_label=production_label, explicit=explicit, release_date=release_date, num_stars=num_stars)
	       artist = Artist.objects.create(name="Frank Sinatra", country="USA", num_stars=4)
	       genre = Genre.objects.create(name="oldies")
	       album.artist.add(artist)
	       album.genre.add(genre)
	       return album

class AlbumViewTests(TestCase):

	def setUp(self):

		user = User.objects.create_user(username="stephen", password="password")
		self.assertEqual(User.objects.all().count(), 1)

	def test_album_detail_view_GET_request(self):

		self.assertTrue(self.client.login(username='stephen', password='password'))
		album = create_album(title="Sinatra's Greatest Hits", production_label="", explicit=False, release_date="1999-12-25", num_stars=4)
                response = self.client.get(reverse("edit_album_detail", args=(album.id,)))
		for template in response.templates:
			self.assertEqual(template.name, 'edit.html')
		self.assertContains(response, 'form')

	def test_album_detail_view_POST_request(self):
                artist = [Artist.objects.create(name="Frank Sinatraz", country="CAN", num_stars=5), Artist.objects.create(name="Corey Taylor", country="USA", num_stars=4)]
		genre = [Genre.objects.create(name="oldies"), Genre.objects.create(name="jazz")]
                self.assertTrue(self.client.login(username='stephen', password='password'))
                album = create_album(title="Sinatra's Greatest Hits", production_label="", explicit=False, release_date="1999-12-25", num_stars=4)
                response = self.client.post(reverse("edit_album_detail", args=(album.id,)), data={'title': 'Frank Sinatras Greatest Hits', 'artist': artist[1], 'genre': genre[1], 'production_label':'Interscope', 'explicit': False, 'release_date':'1999-12-25', 'num_stars':5})
                for template in response.templates:
                        self.assertEqual(template.name, 'thanks.html')

	def test_album_add_view_GET_request(self):

		self.assertTrue(self.client.login(username='stephen', password='password'))
		#album = create_album(title="Sinatra's Greatest Hits", production_label="", explicit=False, release_date="1999-12-25", num_stars=4)
		response = self.client.get(reverse("add_album"))
		for template in response.templates:
			self.assertEqual(template.name, 'add.html')
	
	def test_album_add_view_POST_request(self):

                self.assertTrue(self.client.login(username='stephen', password='password'))
                artist = [Artist.objects.create(name="Lionel Ritchie", country="USA", num_stars=5), Artist.objects.create(name="Eric Clapton", country="USA", num_stars=5)]
		genre = [Genre.objects.create(name="pop"), Genre.objects.create(name="soul")]
                response = self.client.post(reverse("add_album"), data={'title': 'Frank Sinatras Greatest Hits', 'artist': artist[1], 'genre': genre[1], 'production_label': 'Interscope', 'explicit': False, 'release_date': '1999-12-25', 'num_stars':5})
                for template in response.templates:
                        self.assertEqual(template.name, 'thanksadd.html')

class ThanksAddViewTests(TestCase):

	def test_thanks_add_view_GET_request(self):

		response = self.client.get(reverse("thanks_add"))

class ThanksViewTests(TestCase):
	
	def test_thanks_view_GET_request(self):
	
		response = self.client.get(reverse("thanks"))

class test_artist_detail(TestCase):

    def user_is_authenticated(self):
        self.assertTrue(request.user.is_authenticated())

    def method_is_POST(self):
	self.assertTrue(request.method == POST)
	
def create_genre(name,style,time_period, origins,critical_reactions):
  artist1 = Artist.objects.create(name="Black eyed peas",country="USA",num_stars=5)
  genre = Genre.objects.create(name=name,style=style,time_period=time_period,origins=origins,critical_reactions=critical_reactions)
  genre.notable_artists.add(artist1)
  return genre

class GenreViewTest(TestCase):

    def setUp(self):

     user=User.objects.create_user('rachel','rbp45@drexel.edu','testing123')
     self.client.login(username='rachel',password='testing123')


    def test_genre_add_view_GET_request(self):

      response = self.client.get(reverse("add_genre"))
      for template in response.templates:
        self.assertEqual(template.name, 'add.html')


    def test_genre_add_view_POST_request(self):


      response = self.client.post(reverse("add_genre"), data={'name': 'R&B', 'style':'Jazz', 'time_period':'1940s-1950s','origins':'United States','critical_reactions':'Perfect'})
      for template in response.templates:
        self.assertEqual(template.name, 'thanksadd.html')



      response=self.client.post('/discography/add/genre/',{'name':'rock'})

      self.assertEqual(response['Location'],'http://testserver/discography/add/thanks/')
      self.assertEqual(response.status_code,302)

    def test_genre_detail_view_GET_request(self):
       artist2 = Artist.objects.create(name="Louis Armstrong",country="USA",num_stars=5)

       genre = Genre.objects.create(name='Jazz',style='null',time_period='null',origins='null',critical_reactions='Sensational')
       genre.notable_artists.add(artist2)
       response=self.client.get(reverse("edit_genre_detail",args=(genre.id,)))
       for template in response.templates:
         self.assertEqual(template.name,'edit.html')

       self.assertContains(response,'form')



    def test_genre_detail_view_POST_request(self):
       artist2 = Artist.objects.create(name="Louis Armstrong",country="USA",num_stars=5)

       genre = Genre.objects.create(name='Jazz',style='null',time_period='null',origins='null',critical_reactions='Sensational')
       genre.notable_artists.add(artist2)
       response=self.client.post(reverse("edit_genre_detail",args=(genre.id,)),data={'name':'Jazz','style':'Blues,Ragtime','time_period':'Early 1910s','origins':'New Orleans'})

       for template in response.templates:
         self.assertEqual(template.name,'thanks.html')


class TrackViewTest(TestCase):


    def setUp(self):

     user=User.objects.create_user('rachel','rbp45@drexel.edu','testing123')
     self.client.login(username='rachel',password='testing123')


    def test_track_add_view_GET_request(self):

     response=self.client.get(reverse("add_track"))

     for template in response.templates:
        self.assertEqual(template.name, 'add.html')

    def test_track_add_view_POST_request(self):

     artist = Artist.objects.create(name="Black eyed peas",country="USA",num_stars=5)
     artist1=Artist.objects.all()[0]

     response=self.client.post(reverse("edit_track_detail",args=(track1.id,)),data={'title':'The Time'})

     for template in response.templates:
         self.assertEqual(template.name,'thanks.html')





