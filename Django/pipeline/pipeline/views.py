from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is a Laying of Pipeline</h1>")

def home(request):
    return HttpResponse("This is a Home Page")

def about(request):
    return HttpResponse("This is a about Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact Page")