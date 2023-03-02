#rendering a html files

from django.shortcuts import render

def index(request):
   return render(request,'index.html')

def about(request):
    params = {'name':'Sudarshan','place':'pune'}    #extra variable
    return render(request,'about.html', params)