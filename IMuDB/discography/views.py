from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, render
from discography.models import Artist, ArtistForm, Album, AlbumForm, Track, TrackForm, Genre, GenreForm, Award, AwardForm, Credit, CreditForm
from django.template import RequestContext
from django.core.urlresolvers import reverse

def artist_detail(request, artist_id):
	p = get_object_or_404(Artist, pk=artist_id)
	if request.method == 'POST':
		form = ArtistForm(request.POST, instance=p)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/discography/edit/thanks')
	else:
        	form = ArtistForm(instance=p)
    	return render_to_response('edit.html', { 'artist': p, 'form': form}, context_instance=RequestContext(request))

def album_detail(request, album_id):
        p = get_object_or_404(Album, pk=album_id)
        if request.method == 'POST':
                form = AlbumForm(request.POST, instance=p)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/discography/edit/thanks')
        else:
                form = AlbumForm(instance=p)
        return render_to_response('edit.html', { 'album': p, 'form': form}, context_instance=RequestContext(request))

def track_detail(request, track_id):
        p = get_object_or_404(Track, pk=track_id)
        if request.method == 'POST':
                form = TrackForm(request.POST, instance=p)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/discography/edit/thanks')
        else:
                form = TrackForm(instance=p)
        return render_to_response('edit.html', { 'track': p, 'form': form}, context_instance=RequestContext(request))

def genre_detail(request, genre_id):
        p = get_object_or_404(Genre, pk=genre_id)
        if request.method == 'POST':
                form = GenreForm(request.POST, instance=p)
                if form.is_valid():
			import pdb; pdb.set_trace()
                        form.save()
                        return HttpResponseRedirect('/discography/edit/thanks')
        else:
                form = GenreForm(instance=p)
        return render_to_response('edit.html', { 'genre': p, 'form': form}, context_instance=RequestContext(request))

def credit_detail(request, credit_id):
        p = get_object_or_404(Credit, pk=credit_id)
        if request.method == 'POST':
                form = CreditForm(request.POST, instance=p)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/discography/edit/thanks')
        else:
                form = CreditForm(instance=p)
        return render_to_response('edit.html', { 'credit': p, 'form': form}, context_instance=RequestContext(request))

def award_detail(request, award_id):
        p = get_object_or_404(Award, pk=award_id)
        if request.method == 'POST':
                form = AwardForm(request.POST, instance=p)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/discography/edit/thanks')
        else:
                form = AwardForm(instance=p)
        return render_to_response('edit.html', { 'award': p, 'form': form}, context_instance=RequestContext(request))


def thanks(request):
	#artist = get_object_or_404(Artist, pk=artist_id)
	return render(request, 'thanks.html', {"foo": "bar"})
