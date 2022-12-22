from ipware import get_client_ip
from django.http import HttpResponse
import requests
from .models import Ips

class IPIsValid:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        
        Ips(ip=ip).save()

        response = self.get_response(request)

        return response
            