from django.http import HttpResponse
from mainapp.generator import StringGenerator
import sys
import requests
import json

generator = StringGenerator()
if not "migrate" in sys.argv:
    generator.start()

def returnStringAndTimestamp(request):
    response = requests.get("http://pingpong-app:3000/pongcount").json()
    pongs = response["pong"]
    return HttpResponse(f"{generator.timestamp} {generator.random_string}\nPing / Pongs: {pongs}", content_type="text/plain")
