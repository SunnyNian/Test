import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# tensorflow is cheat


class Point():

    points = []

    def __init__(self, x, y):
        try:

            if type(x) is list and type(y) is list:
                self.x = x
                self.y = y
                Point.points.append(self)
                Point.plotdisplay()
                pass

            elif (type(x) is int) and (type(y) is int):
                print("yes1")
                if x >= 0 and y >= 0:
                    print("yes")
                    self.x = x
                    self.y = y
                    Point.points.append(self)
                    Point.plotdisplay()
                else:
                    print("Invalid data point. Both X and Y must be greater than 1.")

            else:
                del self

        except ValueError:
            print("Invalid data point. X and Y should be integers or floats, and should be both greater than 1.")

    def __str__(self):
        pass

    @staticmethod
    def plotdisplay():
        x = []
        y = []

        for i in Point.points:
            if type(i) is list:
                for j in i:
                    x.append(i.j)
                    i.y.append(j)
            else:
                x.append(i.x)
                y.append(i.y)
                print(x)
                print(y)

        x_asarray = np.asarray(x)
        y_asarray = np.asarray(y)

        print(type(y_asarray))

        graph, test = plt.subplots()
        test.plot(x_asarray, y_asarray, 'ko')

        plt.ylim(0, 100)
        plt.xlim(0, 100)

        test.set(xlabel='x', ylabel='y', title='aa')
        test.grid()

        graph.savefig("graph.png")
        plt.show()







