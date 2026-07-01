import tkinter as tk

from views.menu import MainMenu


root = tk.Tk()
root.title("Teleturniej")
root.geometry("1280x720")
root.resizable(False, False)

app = MainMenu(root)
app.pack(fill="both", expand=True)

root.mainloop()