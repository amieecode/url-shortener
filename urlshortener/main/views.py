from django.http import HttpResponse
from django.shortcuts import render
import pyshorteners

# Create your views here.
def shorten(request, url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return HttpResponse(f'Shortened URL: <a href="shortened_url">{shortened_url}</a>')

def index(request):
    return render(request, 'main/index.html')

def shorten_post(request):
    return shorten(request, request.POST['url'])