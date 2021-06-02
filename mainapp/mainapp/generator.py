from time import sleep
from datetime import datetime
from random import choice
from string import ascii_lowercase

def generate_string():
    random_string = "".join((choice(ascii_lowercase) for i in range (0, 10)))
    return random_string