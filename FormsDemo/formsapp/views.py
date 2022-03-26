from django.shortcuts import render
from . import forms

def userRegistrationForm(request):
    form=forms.UserRegistration()
    form_dict={'form':form}
    if request.method=='POST':
        form=forms.UserRegistration(request.POST)
        form_dict={'form':form}
        if form.is_valid():
            print("Form is valid")
            print('Vezeték Név:', form.cleaned_data['firstName'])
            print('Kereszt Név:', form.cleaned_data['lastName'])
            print('Email Cím:', form.cleaned_data['email'])
            print('Neme:', form.cleaned_data['gender'])
    return render(request,'formsdemo/userregistration.html',form_dict)