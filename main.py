import tkinter as tk
from tkinter import *


def shut_down():
    root.destroy()

root = Tk()
root.title("Apka")

mainframe = tk.Frame(root)



loop_end = True
counter = 0
while root.winfo_exists():
    shut = str(input("Write shut if you want to close app\n"))
    shut = shut.lower()
    shut = shut.replace(" ","")
    if shut == "shut":
        shut_down()
        break

root.mainloop()