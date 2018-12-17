import tkinter as tk
from tkinter import ttk


class Test:
    def __init__(self):
        self.parent = tk.Tk()
        self.entry = ttk.Entry(master=self.parent)
        self.entry.pack()

        self.button = ttk.Button(master=self.parent, command=self.retrieve, text="Print it!")
        self.button.pack(side="left")

        self.text = tk.Text(master=self.parent, height=1, width=5)
        self.text.pack(side="bottom")

        self.text.insert("END", "test")

    def retrieve(self):
        print(self.entry.get())
        self.entry.delete(0, END)
        self.text.delete('1.0', END)


a = Test()

tk.mainloop()




