from tkinter import filedialog
from platform import system
from os.path import expanduser

def vibe_check():
    global home
    if system() == "Linux" or system() == "Darwin":
        home = expanduser("~")
        return home
    else:
        print("Ainda não oferecemos suporte à windows, boa sorte lol.")
        quit()