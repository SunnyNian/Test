import tkinter as tk
from tkinter import ttk


class Test:

    points = []

    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("Linear Regression")
        self.parent['padx'] = 5
        self.parent['pady'] = 5
        self.time_frame = None
        self.point_x = None
        self.x_label = None
        self.x_domain_label = None
        self.point_y = None
        self.y_label = None
        self.y_domain_label = None
        self.point_create = None
        self.point_reset = None
        self.variable_frame = None
        self.learning_rate = None
        self.learning_rate_label = None
        self.learning_rate_enter = None
        self.learning_rate_set = None
        self.settings_frame = None
        self.create()

    def create(self):
        self.combobox()

    def combobox(self):

        # Frame for the point plotting part.
        self.time_frame = ttk.LabelFrame(master=self.parent, text="Plot a Point", relief=tk.RIDGE)
        self.time_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.x_label = ttk.Label(master=self.time_frame, text="X :")
        self.x_label.grid(row=1, column=1, sticky=tk.E)

        self.point_x = tk.Spinbox(master=self.time_frame, from_=0, to=99, width=6, justify=tk.RIGHT, repeatinterval=18)
        self.point_x.grid(row=1, column=2, sticky=tk.E)

        self.y_label = ttk.Label(master=self.time_frame, text="Y :")
        self.y_label.grid(row=2, column=1, sticky=tk.E)

        self.point_y = tk.Spinbox(master=self.time_frame, from_=0, to=99, width=6, justify=tk.RIGHT, repeatinterval=18)
        self.point_y.grid(row=2, column=2, sticky=tk.E)

        self.point_create = ttk.Button(master=self.time_frame, text="Add", width=7, command=self.createPoint)
        self.point_create.grid(row=1, column=3, columnspan=2, sticky=tk.S, padx=22)

        self.point_reset = ttk.Button(master=self.time_frame, text="Reset", width=7, command=self.resetPoint)
        self.point_reset.grid(row=2, column=3, columnspan=2, sticky=tk.S, padx=22)

        self.x_domain_label = ttk.Label(master=self.time_frame, text="0 ≤ X ≤ 99, X ϵ Z")
        self.x_domain_label.grid(row=1, column=5)

        self.y_domain_label = ttk.Label(master=self.time_frame, text="0 ≤ Y ≤ 99, Y ϵ Z")
        self.y_domain_label.grid(row=2, column=5)

        # Frame for linear regression variables
        self.variable_frame = ttk.LabelFrame(master=self.parent, text="Regression Variables", relief=tk.RIDGE)
        self.variable_frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.learning_rate_label = ttk.Label(master=self.variable_frame, text="α :")
        self.learning_rate_label.grid(row=1, column=1, sticky=tk.E)

        self.learning_rate = tk.Scale(master=self.variable_frame, width=6, from_=0, to=1, length=160, tickinterval=1,
                                      resolution=0.01, orient=tk.HORIZONTAL, command=self.learningRate)
        self.learning_rate.grid(row=1, column=2, sticky=tk.E + tk.N)

        self.learning_rate_enter = ttk.Entry(master=self.variable_frame, width=4)
        self.learning_rate_enter.grid(row=1, column=3, sticky=tk.E + tk.W)

        self.learning_rate_set = ttk.Button(master=self.variable_frame, width=7, text="Set α", command=self.setLR)
        self.learning_rate_set.grid(row=1, column=4)

        #Frame for already set stuff
        self.settings_frame = ttk.LabelFrame(master=self.parent, text="Points and Settings", relief=tk.RIDGE)
        self.settings_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.S + tk.N, padx=10)

        self.points = ttk.Combobox(master=self.settings_frame, width=7)
        self.points['values'] = Test.points
        self.points.grid(row=1, column=2)

        self.points_label = ttk.Label(master=self.settings_frame, text="Plotted Points :")
        self.points_label.grid(row=1, column=1)

        self.delete_point = ttk.Button(master=self.settings_frame, text="Delete", command=self.delPoint)
        self.delete_point.grid(row=1, column=3, padx = 3)

    def delPoint(self):
        print(self.points.get())
        Test.points.remove(self.points.get())
        self.points['values'] = Test.points
        self.points.delete(0, "end")
        self.points.insert(0, "")
        return


    def learningRate(self, learn):
        print("Learning rate (α): {}".format(learn))
        self.learning_rate_enter.delete(0, "end")
        self.learning_rate_enter.insert(0, learn)

    def setLR(self):
        lr = float(self.learning_rate_enter.get())
        if lr > 1:
            lr = 1
            self.learning_rate_enter.delete(0, "end")
            self.learning_rate_enter.insert(0, 1.00)
        elif lr < 0:
            lr = 0
            self.learning_rate_enter.delete(0, "end")
            self.learning_rate_enter.insert(0, 0.00)
        print("Learning rate (α): {}".format(lr))
        self.learning_rate.set(lr)


    def createPoint(self):
        print("({}, {})".format(self.point_x.get(), self.point_y.get()))
        Test.points.append(self.point_x.get() + "," + self.point_y.get())
        Test.points.sort()
        self.points['values'] = Test.points

    def resetPoint(self):
        self.point_x.delete(0, "end")
        self.point_x.insert(0, 0)
        self.point_y.delete(0, "end")
        self.point_y.insert(0, 0)

    def retrieve(self):
        print(self.entry.get())


a = Test()

tk.mainloop()
