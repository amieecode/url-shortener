import random 
import string 
from django.http import Http404
from django.utils import timezone
from .models import LinkMapping

def shorten(url):
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = LinkMapping(original_url=url, hashing=random_hash, creation_date=timezone.now())
    mapping.save()
    return random_hash

def load_url(url_hash):
    try:
        return LinkMapping.objects.get(hashing=url_hash)
    except LinkMapping.DoesNotExist:
        raise Http404("Shortened URL not found")

