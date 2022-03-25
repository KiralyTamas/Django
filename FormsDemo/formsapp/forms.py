from django import forms

class UserRegistration(forms.Form):
    firstName=forms.CharField(label='Vezeték Név')
    lastName=forms.CharField(label='Kereszt Név')
    email=forms.EmailField(label='Email Cím')