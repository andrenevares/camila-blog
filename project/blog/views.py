from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    title = "Home"
    return render (request, 'blog/home.html', {'title': title})


