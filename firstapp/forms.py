from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cluster, Nutzer, Reservation

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
				
class ClusterForm(ModelForm):
	class Meta:
		model = Cluster
		fields = ('tag_system', 'title', 'Beschreibung', 'availability')

class RegisterForm(UserCreationForm):
#	matrikelnummer = forms.IntegerField(max_value="1000000")

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		#user.matrikelnummer = self.cleaned_data['matrikelnummer']
		if commit:
			user.save()
		return user

#help ReservationForm so that User can only interact with date (no change to given cluster or user)
class DateInput(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ['date']

class ReservationForm(ModelForm):
	class Meta:
		model = Reservation
		fields = ['cluster', 'date', 'user']
	date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y', )
        )
	
""" 	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(ReservationForm, self).__init__(*args, **kwargs)
		self.fields[''] """