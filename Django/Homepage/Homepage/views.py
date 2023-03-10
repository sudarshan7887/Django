from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'",.<>/?@#$%*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed punctuation','analyzed_text':analyzed}

        #Analyze the text   
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("error")


