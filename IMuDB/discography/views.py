from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render
from discography.models import Artist, ArtistForm, Album, AlbumForm, Track, TrackForm, TrackSearchForm, Genre, GenreForm, Award, AwardForm, Credit, CreditForm, ArtistSearchForm, GenreSearchForm, AlbumSearchForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from discography.forms import SearchChoiceForm, CreditSearchForm, AwardSearchForm
from django.views.generic.edit import FormView

def artist_detail(request, artist_id):
	if request.user.is_authenticated():
		p = get_object_or_404(Artist, pk=artist_id)
		if request.method == 'POST':
			form = ArtistForm(request.POST, instance=p)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/discography/edit/thanks')
		else:
        		form = ArtistForm(instance=p)
    		return render_to_response('edit.html', { 'artist': p, 'form': form}, context_instance=RequestContext(request))
	else:
		return render(request, 'notauthenticated.html')
def album_detail(request, album_id):
	if request.user.is_authenticated():
        	p = get_object_or_404(Album, pk=album_id)
        	if request.method == 'POST':
                	form = AlbumForm(request.POST, instance=p)
                	if form.is_valid():
                        	form.save()
                        	return HttpResponseRedirect('/discography/edit/thanks')
        	else:
                	form = AlbumForm(instance=p)
        	return render_to_response('edit.html', { 'album': p, 'form': form}, context_instance=RequestContext(request))
	else:
		return render(request, 'notauthenticated.html')
def track_detail(request, track_id):
	if request.user.is_authenticated():
		p = get_object_or_404(Track, pk=track_id)
        	if request.method == 'POST':
                	form = TrackForm(request.POST, instance=p)
                	if form.is_valid():
                        	form.save()
                        	return HttpResponseRedirect('/discography/edit/thanks')
        	else:
                	form = TrackForm(instance=p)
        	return render_to_response('edit.html', { 'track': p, 'form': form}, context_instance=RequestContext(request))
	else:
		return render(request, 'notauthenticated.html')
def genre_detail(request, genre_id):
	if request.user.is_authenticated():
        	p = get_object_or_404(Genre, pk=genre_id)
        	if request.method == 'POST':
                	form = GenreForm(request.POST, instance=p)
                	if form.is_valid():
                        	form.save()
                        	return HttpResponseRedirect('/discography/edit/thanks')
        	else:
                	form = GenreForm(instance=p)
        	return render_to_response('edit.html', { 'genre': p, 'form': form}, context_instance=RequestContext(request))
	else:
		return render(request, 'notauthenticated.html')
def credit_detail(request, credit_id):
	if request.user.is_authenticated():
        	p = get_object_or_404(Credit, pk=credit_id)
        	if request.method == 'POST':
                	form = CreditForm(request.POST, instance=p)
                	if form.is_valid():
                        	form.save()
                        	return HttpResponseRedirect('/discography/edit/thanks')
        	else:
                	form = CreditForm(instance=p)
        	return render_to_response('edit.html', { 'credit': p, 'form': form}, context_instance=RequestContext(request))
	else:
		return render(request, 'notauthenticated.html')
def award_detail(request, award_id):
	if request.user.is_authenticated():
        	p = get_object_or_404(Award, pk=award_id)
        	if request.method == 'POST':
                	form = AwardForm(request.POST, instance=p)
                	if form.is_valid():
                        	form.save()
                        	return HttpResponseRedirect('/discography/edit/thanks')
        	else:
                	form = AwardForm(instance=p)
        	return render_to_response('edit.html', { 'award': p, 'form': form}, context_instance=RequestContext(request))
	else:
		return render(request, 'notauthenticated.html')
def artist_add(request):
	if request.user.is_authenticated():
	
		if request.method == 'POST':
			f = ArtistForm(request.POST)
			if f.is_valid():
	        		f.save()
				return HttpResponseRedirect('/discography/add/thanks/')
		else:
			f = ArtistForm()
		return render(request, 'add.html', {'form' : f})
	else:
		return render(request, 'notauthenticated.html')
def album_add(request):
	if request.user.is_authenticated():
        	if request.method == 'POST':
                	f = AlbumForm(request.POST)
                	if f.is_valid():
				f.save()
                		return HttpResponseRedirect('/discography/add/thanks/')
        	else:
                	f = AlbumForm()
        	return render(request, 'add.html', {'form' : f})
	else:
		return render(request, 'notauthenticated.html')
def track_add(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
                	f = TrackForm(request.POST)
                	if f.is_valid():
				f.save()
                		return HttpResponseRedirect('/discography/add/thanks/')
        	else:
                	f = TrackForm()
        	return render(request, 'add.html', {'form' : f})
	else:
		return render(request, 'notauthenticated.html')
def genre_add(request):
	if request.user.is_authenticated():
        	if request.method == 'POST':
                	f = GenreForm(request.POST)
                	if f.is_valid():
				f.save()
                		return HttpResponseRedirect('/discography/add/thanks/')
        	else:
                	f = GenreForm()
        	return render(request, 'add.html', {'form' : f})
	else:
		return render(request, 'notauthenticated.html')
def credit_add(request):
	if request.user.is_authenticated():
        	if request.method == 'POST':
                	f = CreditForm(request.POST)
                	if f.is_valid():
				f.save()
                		return HttpResponseRedirect('/discography/add/thanks/')
        	else:
                	f = CreditForm()
        	return render(request, 'add.html', {'form' : f})
	else:
		return render(request, 'notauthenticated.html')
def award_add(request):
	if request.user.is_authenticated():
        	if request.method == 'POST':
                	f = AwardForm(request.POST)
                	if f.is_valid():
				f.save()
                		return HttpResponseRedirect('/discography/add/thanks/')
        	else:
                	f = AwardForm()
        	return render(request, 'add.html', {'form' : f})
	else:
		return render(request, 'notauthenticated.html')

class SearchChoiceView(FormView):
	template_name = 'searchchoice.html'
	form_class = SearchChoiceForm
	#success_url = '/search/query/'

	def form_valid(self, form):
			if form.cleaned_data['choice'] == 'Art':
				return HttpResponseRedirect('/discography/search/artist/')
			if form.cleaned_data['choice'] == 'Alb':
				return HttpResponseRedirect('/discography/search/album/')
			if form.cleaned_data['choice'] == 'Gen':
				return HttpResponseRedirect('/discography/search/genre/')
			if form.cleaned_data['choice'] == 'Tra':
				return HttpResponseRedirect('/discography/search/track/')
			if form.cleaned_data['choice'] == 'Cre':
				return HttpResponseRedirect('/discography/search/credit/')
			if form.cleaned_data['choice'] == 'Awa':
				return HttpResponseRedirect('/discography/search/award/')

def search_artist(request):
        if request.method == 'POST':
                f = ArtistSearchForm(request.POST)
		if f.is_valid():
			q = Artist.objects.filter(name = f.cleaned_data['name'])
                	return render(request, 'artistsearchresults.html', {'results' : q})
        else:
                f = ArtistSearchForm()
        return render(request, 'artistsearch.html', {'form' : f})

def search_genre(request):
        if request.method == 'POST':
                f = GenreSearchForm(request.POST)
                if f.is_valid():
                        q = Genre.objects.filter(name = f.cleaned_data['name'])
                        return render(request, 'genresearchresults.html', {'results' : q})
        else:
                f = GenreSearchForm()
        return render(request, 'genresearch.html', {'form' : f})

def search_album(request):
        if request.method == 'POST':
                f = AlbumSearchForm(request.POST)
                if f.is_valid():
                        q = Album.objects.filter(title = f.cleaned_data['title'])
                        return render(request, 'albumsearchresults.html', {'results' : q})
        else:
                f = AlbumSearchForm()
        return render(request, 'albumsearch.html', {'form' : f})

def search_track(request):
        if request.method == 'POST':
                f = TrackSearchForm(request.POST)
                if f.is_valid():
                        q = Track.objects.filter(title = f.cleaned_data['title'])
                        return render(request, 'tracksearchresults.html', {'results' : q})
        else:
                f = TrackSearchForm()
        return render(request, 'tracksearch.html', {'form' : f})

def search_credit(request):
        if request.method == 'POST':
                f = CreditSearchForm(request.POST)
                if f.is_valid():
                        q = Credit.objects.filter(album__title = f.cleaned_data['album'])
                        return render(request, 'creditsearchresults.html', {'results' : q})
        else:
                f = CreditSearchForm()
        return render(request, 'creditsearch.html', {'form' : f})

def search_award(request):
        if request.method == 'POST':
                f = AwardSearchForm(request.POST)
                if f.is_valid():
                        q = Award.objects.filter(awardcategory__name = f.cleaned_data['awardcategory'])
                        return render(request, 'awardsearchresults.html', {'results' : q})
        else:
                f = AwardSearchForm()
        return render(request, 'awardsearch.html', {'form' : f})




def thanks_add(request):
	return render(request, 'thanksadd.html', {"foo":"bar"})

def thanks(request):
	#artist = get_object_or_404(Artist, pk=artist_id)
	return render(request, 'thanksedit.html', {"foo": "bar"})
