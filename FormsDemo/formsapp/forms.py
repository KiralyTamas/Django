from django import forms

class UserRegistration(forms.Form):
    GENDER=[('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField(label='Vezeték Név')
    lastName=forms.CharField(label='Kereszt Név')
    email=forms.EmailField(label='Email Cím')
    password=forms.CharField(widget=forms.PasswordInput, label='Jelszó')
    gender=forms.CharField(widget=forms.Select(choices=GENDER),label='Neme')
    ssn=forms.IntegerField()
    
    def clean_firstName(self):
        inputfirstName=self.cleaned_data['firstName']
        if len(inputfirstName)>8:
            raise forms.ValidationError('Maximális karakterszám: 8')
        return inputfirstName
    
    def clean_password(self):
        pass_len=4
        inputpassword=self.cleaned_data['password']
        if len(inputpassword)<pass_len:
            raise forms.ValidationError(f'A jelszónak minimum {pass_len} karakter hosszúnak kell lennie!')
        return inputpassword
        