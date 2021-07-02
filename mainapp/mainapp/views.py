from django.http import HttpResponse
from mainapp.generator import StringGenerator
import sys
import os.path

generator = StringGenerator()
if not "migrate" in sys.argv:
    generator.start()

directory = "./files/"
filename = "pongs.txt"
file_path = os.path.join(directory, filename)

def returnStringAndTimestamp(request):
    try:
        with open(file_path) as file:
            pongs = file.read()
            return HttpResponse(f"{generator.timestamp} {generator.random_string}\n{pongs}", content_type="text/plain")
    except:
        print("file not found")