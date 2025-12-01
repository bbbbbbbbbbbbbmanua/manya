import tkinter as tk
from tkinter import *

root =  tk.Tk()

root.title("Моё первое окно")
root.geometry("900x900")
root.iconbitmap(default="subashich.ico")

Label_1_Hello_world = Label(text = "Hello world!!!")
Label_1_Hello_world.pack()

root.mainloop()