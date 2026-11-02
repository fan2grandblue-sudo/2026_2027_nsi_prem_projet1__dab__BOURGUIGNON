from time import *
#color code : \033[38;5;40m
def print_anim(text):
    for character in text:
        print(character, end="", flush=True)
        sleep(0.03)

def loading(duration, dots):
    for n in range(dots):
        print("\033[38;5;40m.", end="  ", flush=True)
        sleep(duration/dots)
    print("\n")

def longline():
    for n in range(100):
        print("\033[38;5;40m_", end="_", flush=True)
    print("\n")

longline()
loading(1, 68)
print_anim("this text is a test")