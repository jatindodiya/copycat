from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Tk  # Python 3


class mainframe:
    def __init__(self):
        self.root = Tk()
        self.root.title('Copycat')
        self.root.resizable(0, 0)
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root["bg"] = "white"
        self.root.minsize(150, 50)
        self.root.maxsize(3000, 200)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.x = screen_width - 180
        self.y = screen_height // 2 - 80
        self.position_window()
        self.root.after(100, self.update)
        self.i = 0

        self.mainframe = Frame(self.root, padx=0, pady=0, bg="green")
        self.mainframe.grid_columnconfigure(0, weight=2)
        self.mainframe.grid_columnconfigure(1, weight=1)
        self.mainframe.pack()

        self.text_entry = tk.Text(self.mainframe, width=25, height=1)
        self.text_entry.configure(font=('Courier', 11))
        self.text_entry.grid(column=0, row=0, padx=5, pady=5)

        self.copy_button = ttk.Button(self.mainframe, text="Copy", command=self.copytext, width=5)
        self.copy_button.grid(column=0, row=1, padx=5, pady=5)

        self.root.mainloop()

    def copytext(self):
        message = str(self.text_entry.get(1.0, "end-1c"))
        self.root.clipboard_clear()
        self.root.clipboard_append(message)

    def update(self):
        try:
            clipboard = self.root.clipboard_get()
            message = str(self.text_entry.get(1.0, "end-1c"))
            print(clipboard, message)
            if clipboard == message and message != "":
                self.mainframe.config(bg="green")
            else:
                self.mainframe.config(bg="red")

        except:
            self.mainframe.config(bg="blue")

        self.root.after(200, self.update)

    def changeColor(self, color):
        self.root["bg"] = color

    def position_window(self):
        self.root.geometry('+%d+%d' % (self.x, self.y))


if __name__ == "__main__":
    mainframe()
