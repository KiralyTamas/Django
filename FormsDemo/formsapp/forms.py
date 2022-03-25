from django import forms

class UserRegistration(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField(label='Vezeték Név')
    lastName=forms.CharField(label='Kereszt Név')
    email=forms.EmailField(label='Email Cím')
    password=forms.CharField(widget=forms.PasswordInput)
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    ssn=forms.IntegerField()
    
    def clean_firstName(self):
        inputfirstName=self.cleaned_data['firstName']
        if len(inputfirstName)>8:
            raise forms.ValidationError('Maximális karakterszám: 8')
        return inputfirstName