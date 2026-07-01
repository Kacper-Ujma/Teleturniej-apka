import tkinter as tk


class MainMenu(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.configure(bg="#111111")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self,
            text="TELETURNIEJ",
            font=("Segoe UI", 36, "bold"),
            fg="white",
            bg="#111111"
        )

        title.pack(pady=120)


        start_button = tk.Button(
            self,
            text="START",
            font=("Segoe UI", 18, "bold"),
            width=15,
            height=2,
            command=self.start_game
        )

        start_button.pack(pady=15)


        exit_button = tk.Button(
            self,
            text="EXIT",
            font=("Segoe UI", 18, "bold"),
            width=15,
            height=2,
            command=self.parent.destroy
        )

        exit_button.pack()

    def start_game(self):
        print("Game started")