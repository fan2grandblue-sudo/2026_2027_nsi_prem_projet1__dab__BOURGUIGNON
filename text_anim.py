from time import *
from sys import *
#color code : \033[38;5;40m
def print_anim(text):
    for character in text:
        print(character, end="", flush=True)
        sleep(0.1)

def load_dots(duration, dots):
    for n in range(dots):
        print("\033[38;5;40m.", end="  ", flush=True)
        sleep(duration/dots)
    print("\n")

def load_bar(duration, length):
    print("Loading...")
    for n in range(length):
        bar = "█" * (n // 5) + "▒" * (20 - n // 5)
        sys.stdout.write(f"r{bar} {n//length*100}%")
        sleep(duration/length)
    print("\n")

def longline():
    for n in range(100):
        print("\033[38;5;40m_", end="_", flush=True)
    print("\n")

load_bar(5, 100, 1)
print_anim("this text is a test")