from django.shortcuts import render

def renderTemplate(request):
    myDict={"name":"Király Tamás"}
    return render(request, 'templatesapp/first_template.html', myDict)

def renderEmployee(request):
    myDict={"id":123,"name":"King","sal":10000}
    return render(request, 'templatesapp/employee_template.html',myDict)