import os.path
from time import sleep

directory = "./files/"
filename = "hash.txt"
file_path = os.path.join(directory, filename)

while True:
    try:
        with open(file_path) as file:
            hash = file.read()
            print(hash)
    except:
        print("file not found")
    sleep(5)