from django.http import HttpResponse
from mainapp.generator import StringGenerator
import sys

generator = StringGenerator()
if not "migrate" in sys.argv:
    generator.start()

def returnStringAndTimestamp(request):
    return HttpResponse(f"{generator.timestamp} {generator.random_string}", content_type="text/plain")
