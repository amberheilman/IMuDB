from django import forms

class SearchChoiceForm(forms.Form):
	CHOICES = (
		('Gen', 'Genre'),
		('Art', 'Artist'),
		('Alb', 'Album'),
		('Tra', 'Track'),
		('Cre', 'Credit'),
		('Awa', 'Award'),
	)
	choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

class CreditSearchForm(forms.Form):
	album = forms.CharField(max_length=200)

class AwardSearchForm(forms.Form):
	awardcategory = forms.CharField(max_length=200)
