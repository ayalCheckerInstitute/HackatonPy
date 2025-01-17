from django import forms
from django.forms import ModelForm
from .models import Event, Location


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'location', 'host', 'description', 'attendees')
        labels = {
            'name': 'Name',
            'date': 'YYYY-MM-DD HH:MM:SS',
            'location': 'Location',
            'host': 'Host',
            'description': 'Description',
            'attendees': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'host': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Host'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'})
        }


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': 'Name',
            'address': 'Address',
            'zip_code': 'Zip Code',
            'phone': 'Phone',
            'web': 'URL',
            'email_address': 'Email Address'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL address'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }
