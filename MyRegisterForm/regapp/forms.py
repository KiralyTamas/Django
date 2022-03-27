from django import forms
from django.core import validators

class regForm(forms.Form):
    firstName=forms.CharField(validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(20)],label='Vezeték Név')
    lastName=forms.CharField(validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(20)], label='Kereszt Név')
    userName=forms.CharField(validators=[validators.MinLengthValidator(4),validators.MaxLengthValidator(20)], label='Felhasználói Név')
    email=forms.EmailField(validators=[validators.EmailValidator()], label='Email Cím')
    password=forms.CharField(widget=forms.PasswordInput, label='Jelszó')
    
    def clean(self):
        cleaned_data=super().clean()
        inputPassword=cleaned_data['password']
        for letter in inputPassword:
            if letter.isupper():
                return
        else:
            raise forms.ValidationError('Legalább 1 Nagybetűt kell, hogy tartalmazzon a jelszó!')