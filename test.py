import tkinter as tk
from tkinter import ttk


class Test:
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("Linear Regression")
        self.parent['padx'] = 5
        self.parent['pady'] = 5
        self.time_frame = None
        self.point_x = None
        self.x_label = None
        self.point_y = None
        self.y_label = None
        self.point_create = None
        self.point_reset = None
        self.variable_frame = None
        self.learning_rate = None
        self.learning_rate_label = None
        self.create()

    def create(self):
        self.combobox()

    def combobox(self):

        # Frame for the point plotting part.
        self.time_frame = ttk.LabelFrame(master=self.parent, text="Plot a Point", relief=tk.RIDGE)
        self.time_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.x_label = ttk.Label(master=self.time_frame, text="X :")
        self.x_label.grid(row=1, column=1, sticky=tk.E)

        self.point_x = tk.Spinbox(master=self.time_frame, from_=0, to=99, width=6, justify=tk.RIGHT, repeatinterval=30)
        self.point_x.grid(row=1, column=2, sticky=tk.E)

        self.y_label = ttk.Label(master=self.time_frame, text="Y :")
        self.y_label.grid(row=2, column=1, sticky=tk.E)

        self.point_y = tk.Spinbox(master=self.time_frame, from_=0, to=99, width=6, justify=tk.RIGHT, repeatinterval=30)
        self.point_y.grid(row=2, column=2, sticky=tk.E)

        self.point_create = ttk.Button(master=self.time_frame, text="Add", width=7, command=self.createPoint)
        self.point_create.grid(row=1, column=3, columnspan=2, sticky=tk.S, padx=32)

        self.point_reset = ttk.Button(master=self.time_frame, text="Reset", width=7, command=self.resetPoint)
        self.point_reset.grid(row=2, column=3, columnspan=2, sticky=tk.S, padx=32)

        # Frame for linear regression variables
        self.variable_frame = ttk.LabelFrame(master=self.parent, text="Regression Variables", relief=tk.RIDGE)
        self.variable_frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.learning_rate_label = ttk.Label(master=self.variable_frame, text="α :")
        self.learning_rate_label.grid(row=1, column=1, sticky=tk.E)

        self.learning_rate = tk.Scale(master=self.variable_frame, width=6, from_=0, to=1, length=160, tickinterval=1,
                                      resolution=0.01, orient=tk.HORIZONTAL, command=self.learningRate)
        self.learning_rate.grid(row=1, column=2, sticky=tk.E + tk.N)

    def learningRate(self, test):
        print("Learning rate (α): {}".format(self.learning_rate.get()))

    def createPoint(self):
        print("({}, {})".format(self.point_x.get(), self.point_y.get()))

    def resetPoint(self):
        self.point_x.delete(0, "end")
        self.point_x.insert(0, 0)
        self.point_y.delete(0, "end")
        self.point_y.insert(0, 0)

    def retrieve(self):
        print(self.entry.get())


a = Test()

tk.mainloop()
