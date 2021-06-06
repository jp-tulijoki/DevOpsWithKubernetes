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
        while True:
            self.timestamp = datetime.now()
            print(self.timestamp, self.random_string)
            sleep(5)

