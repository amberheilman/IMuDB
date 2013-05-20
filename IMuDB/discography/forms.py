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

