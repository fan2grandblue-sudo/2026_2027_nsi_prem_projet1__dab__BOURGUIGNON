from sys import *
from time import *
print("\033[38;5;40mBOOTING UP")
def print_anim(text):
    for character in text:
        print(character, end="", flush=True)
        sleep(0.08)

def load_dots(duration, dots):
    for n in range(dots):
        print("\033[38;5;40m.", end="  ", flush=True)
        sleep(duration/dots)
    print("\n")

def load_bar(duration, length):
    print("Loading...")
    for n in range(length + 1):
        progress = n / length
        percent = int(progress * 100)
        filled = int(progress * 20)
        bar = "█" * filled + "▒" * (20 - filled)
        stdout.write(f"\r{bar} {percent}%")
        stdout.flush()
        sleep(duration / length)
    sleep(2)
    stdout.flush()
    print("\n\n\n")

def longline():
    for n in range(100):
        print("\033[38;5;40m_", end="_", flush=True)
    print("\n")