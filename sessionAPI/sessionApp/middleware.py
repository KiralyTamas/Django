from django.http import HttpResponse
from django.shortcuts import render

class MiddleWareLifeCycle:
    def __init__(self, get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        print('Before the view is executed')
        response=self.get_response(request)
        print('After the view is executed')
        return response
    
class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self,request,exception):
        if exception.__class__.__name__ =="TemplateDoesNotExist":
            return HttpResponse("<b>Valami baj van a sablon fájlal.</b>")
        elif exception.__class__.__name__ =="NameError":
            return render(request, 'sessionApp/message.html')
        print(exception.__class__.__name__ )
        print(exception)
        return HttpResponse("<b>Valami nagyon katasztrófális történt.</b>")