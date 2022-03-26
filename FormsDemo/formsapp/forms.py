from django import forms
from django.core import validators

class UserRegistration(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField(label='Vezeték Név',validators=
                        [validators.MinLengthValidator(3),validators.MaxLengthValidator(8)])
    lastName=forms.CharField(label='Kereszt Név')
    email=forms.EmailField(label='Email Cím')
    password=forms.CharField(widget=forms.PasswordInput, label='Jelszó')
    gender=forms.CharField(widget=forms.Select(choices=GENDER),label='Neme')
    ssn=forms.IntegerField()
"""
    def clean(self):
        user_cleaned_data=super().clean()
        max_len=8
        pass_len=4
        inputfirstName=user_cleaned_data['firstName']
        if len(inputfirstName)>max_len:
            raise forms.ValidationError(f'Maximális karakterszám: {max_len}')
        inputEmail=user_cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('Nem megfelelő Email formátum')
        inputPassword=user_cleaned_data['password']
        if len(inputPassword)<pass_len:
            raise forms.ValidationError(f'A jelszónak minimum {pass_len} karakter hosszúnak kell lennie!')
        return

    def clean_firstName(self):
        max_len=8
        inputfirstName=self.cleaned_data['firstName']
        if len(inputfirstName)>max_len:
            raise forms.ValidationError(f'Maximális karakterszám: {max_len}')
        return inputfirstName
    
    def clean_email(self):
        inputEmail=self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('Nem megfelelő Email formátum')
        return inputEmail
    
    def clean_password(self):
        pass_len=4
        inputpassword=self.cleaned_data['password']
        if len(inputpassword)<pass_len:
            raise forms.ValidationError(f'A jelszónak minimum {pass_len} karakter hosszúnak kell lennie!')
        return inputpassword

"""