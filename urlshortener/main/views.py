from django.http import HttpResponse
from django.shortcuts import render
import pyshorteners

# Create your views here.
def shorten(request, url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    return HttpResponse(f'Shortened URL: <a href="shortened_url">{shortened_url}</a>')
