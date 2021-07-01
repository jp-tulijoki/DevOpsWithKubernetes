import os.path
from time import sleep
from datetime import datetime
from random import choice
from string import ascii_lowercase
from threading import Thread

class StringGenerator(Thread):
    def __init__(self):
        super(StringGenerator, self).__init__()
        self.random_string = "".join((choice(ascii_lowercase) for i in range (0, 10)))
        self.timestamp = datetime.now()

    def run(self):
        directory = "./files/"
        filename = "hash.txt"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        while True:
            self.timestamp = datetime.now()
            hash = f"{self.timestamp} {self.random_string}"
            with open(file_path, "w") as file:
                file.write(hash) 
            sleep(5)

