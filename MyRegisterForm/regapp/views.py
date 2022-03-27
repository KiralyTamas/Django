from django.shortcuts import render
from . import forms

def registerForm(request):
    message=["Ready to registration?","Your registration is successed :)","The registration was failed"]
    form=forms.regForm()
    form_dict={'form':form,'message':message[0]}
    if request.method=='POST':
        form=forms.regForm(request.POST)
        form_success={'form':form,'message':message[1]}
        form_faild={'form':form,'message':message[2]}
        if form.is_valid():
            print("Your registration is successed :)")
            return render(request,'regapp/regform.html',form_success)
        else:
            return render(request,'regapp/regform.html',form_faild)
    return render(request,'regapp/regform.html',form_dict)