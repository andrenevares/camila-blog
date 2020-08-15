from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render (request, template_name="blog/home.html")
