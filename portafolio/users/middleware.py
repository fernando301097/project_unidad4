from ipware import get_client_ip
from django.http import HttpResponse
import requests




BLACK_LIST = []


def middleware(request):
        ip, is_routable = get_client_ip(request)
        response = get_response(request)
        print("ip", ip)
        print("is_routable", is_routable)
        if str(ip) in BLACK_LIST:
            return HttpResponse("No tienes permisos", status=404)
        else:
            return response
    

class IPIsValid:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        print("ip", ip)
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=40213bf4125645b6b0ef263b4aeaf88f&ip_address=" + ip)
        data = response.json()

        response = self.get_response(request)
        if data["country"] == "Peru":
            return response
        else:
            return HttpResponse("Esto es solo para Peru", status=401)
            