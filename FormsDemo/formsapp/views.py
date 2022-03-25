from django.shortcuts import render
from . import forms

def userRegistrationForm(request):
    form=forms.UserRegistration()
    form_dict={'form':form}
    return render(request,'formsdemo/userregistration.html',form_dict)