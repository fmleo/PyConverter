#!/usr/bin/env python

import tkinter as tk
import os
from utils import *

home = vibe_check()

def openfile(event=None):
    global filename
    filename = filedialog.askopenfilename(
        title="Escolher Arquivo",
        filetypes=(("MP4", "*.mp4"), ("AVI", "*.avi"), ("MOV", "*.mov"), ("MKV", "*.mkv")),
        initialdir=home
    )
    entrada.delete(0, tk.END)
    entrada.insert(0, filename)

def opendir():
    global path
    path = filedialog.askdirectory(
        title="Escolher caminho de saída",
        initialdir=home
    )
    saida.delete(0, tk.END)
    saida.insert(0, path)

def convert():
    path_from = entrada.get()
    print(path_from)
    filename = "".join(path_from.split("/")[-1:]).split(".")[0]
    print(filename)
    path_to = saida.get() if saida.get().endswith("/") else saida.get()+"/"
    file_type_to = tkvar.get().lower()
    if file_type_to != "":
        os.system(f"ffmpeg -i {path_from} {path_to}{filename}.{file_type_to} >/dev/null 2>&1")
        print(f"ffmpeg -i {path_from} {path_to}{filename}.{file_type_to}")
    else:
        label_text.set("Você precisa selecionar um tipo de arquivo.")

w, h = 800, 400
root = tk.Tk()
root.title("PyConverter")
root.geometry(f"{w+20}x{h+20}")

button_input = tk.Button(root, text="Entrada", command=openfile)
button_input.place(anchor="nw", x=10, y=10, height=h/5/2, width=w/4)

button_output = tk.Button(root, text="Saída", command=opendir)
button_output.place(anchor="nw", x=10, y=h/5/2+10, height=h/5/2, width=w/4)

entrada = tk.Entry(root)
entrada.insert(0, " /caminho/para/o/video/a/ser/convertido/")
entrada.place(x=w/4+15, y=10, height=(h/5/2)-5, width=(w-w/4)-5)

saida = tk.Entry(root)
saida.insert(0, " /caminho/para/o/video/convertido/")
saida.place(x=w/4+15, y=(h/5/2)+14, height=(h/5/2)-5, width=(w-w/4)-5)

tkvar = tk.StringVar(root)
escolhas = ["MP4", "AVI", "MOV", "MKV"]
dropdown = tk.OptionMenu(root, tkvar, *escolhas)
dropdown.place(anchor="nw", x=10, y=h/5/2+55, height=h/5/2, width=w/4)

converter = tk.Button(root, text="Converter", command=convert)
converter.place(anchor="ne", x=w+10, y=h/5/2+55, height=h/5/2, width=w/4)

label_text = tk.StringVar()
warning = tk.Label(root, textvariable=label_text)
warning.place(anchor="center", x=w/2, y=h/2)

button_quit = tk.Button(root, text="Sair", command=quit)
button_quit.place(anchor="se", x=w+10, y=h+10, width=w/5, height=h/5)

root.mainloop()