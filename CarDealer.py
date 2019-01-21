try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk


class Car:
    
    a = []
    b = []
    
    def __init__(self, name, Make, Model, Year, Odometer, Colour, Price):
        """
        This initializer function takes all 6 properties of the car and puts it into a list assigned to the object.
        It then passes the function through the condense function.
        :param Make: Desired make of the car, as any data type.
        :param Model: Desired model of the car, as any data type.
        :param Year: Desired year of the car, as any data type.
        :param Odometer: Desired odometer of the car, as any data type.
        :param Colour: Desired colour of the car, as any data type.
        :param Price: Desired price of the car, as any data type.
        """

        self.Script = [Make, Model, Year, Odometer, Colour, Price]
        self.name = name
        self.condense()
        
    def condense(self):
        """
        This function checks object self to see if a car with an already matching script property is present in the list
        a. If it is not, a new item is appending to that list and it is given a corresponding value of 1 in list b. If
        it is already present, then its corresponding value in list b is increased by 1.
        :return: None, as NoneType.
        """
        if self.Script not in Car.a:
            Car.a.append(self.Script)
            Car.b.append(1)
        else:
            for i in Car.a:
                if self.Script == i:
                    Car.b[Car.a.index(i)] = Car.b[Car.a.index(i)] + 1
                    break
                
    def __str__(self):
        """
        When a car object is printed, all of its properties are displayed.
        """
        return "{}".format(self.name)

    @staticmethod
    def findCar(Make, Model, Year, Odometer, Colour, Price):
        """
        When there is an attempt to find a car, the 6 parameters inputted will be compared against all other lists in
        list Car.a until there is a match. If there is, the parameters are outputted along with Car.b's index of the
        Car.a list that matches the input parameters, which is representative of the number of cars.
        :param Make: Desired make of the car, as any data type.
        :param Model: Desired model of the car, as any data type.
        :param Year: Desired year of the car, as any data type.
        :param Odometer: Desired odometer of the car, as any data type.
        :param Colour: Desired colour of the car, as any data type.
        :param Price: Desired price of the car, as any data type.
        :return: None, as NoneType.
        """
        carType = [Make, Model, Year, Odometer, Colour, Price]
        for i in Car.a:
            if carType == i:
                car = Car.b[Car.a.index(carType)]
                print("Car found!\nCar Characterstics:\nBrand: {}\nModel: {}\nYear: {}\nOdometer: {}\nColour: {}\nPrice: {}".format(Make, Model, Year, Odometer, Colour, Price))
                print("\nNumber available: {}".format(car))
                break
        print("Search for car has ended.")

    def deleteCar(self):
        """
        When this method is used with an object, it searches that objects Script property until a match has been found
        in Car.a. When a match is found, the corresponded Car.b value is deleted and then checked if it is equal to 0.
        If it is equal to 0, then both that Car.b value and Car.a value will be deleted, as no other objects will have
        these properties, and then the object itself is deleted. Otherwise, the object itself is deleted.
        :return: None, as NoneType.
        """
        for i in Car.a:
            if self.Script == i:
                Car.b[Car.a.index(i)] = Car.b[Car.a.index(i)] - 1
                if Car.b[Car.a.index(i)] == 0:
                    del Car.b[Car.a.index(i)]
                    del Car.a[Car.a.index(i)]
                break
        del self

    @staticmethod
    def customer(name, phone, income):
        """
        When this static method is called, it displays the name and phone parameter. It then searches all of Car.a's
        cars to find all cars where the price is less than or equal to the given income. Whenever a match is found, it
        is printed. Afterwards, a message signalling the end of this search is printed.
        :param name: Name of customer, as any data type.
        :param phone: Phone number of customer, as any data type.
        :param income: Find all cars with price under this value, as an integer.
        :return: None, as NoneType.
        """
        try:
            print("Searching for cars for {} ({})\n".format(name, phone))
            for i in Car.a:
                if i[5] <= income:
                    print("Car {}:\nBrand: {}\nModel: {}\nYear: {}\nOdometer: {}\nColour: {}\nPrice: {}\n________________________\n".format(Car.a.index(i), i[0], i[1], i[2], i[3], i[4], i[5]))

            print("Search for car has ended.")
        except:
            print("Woops! Something went wrong. Maybe the price wasn't an integer or float?")

class Parent:

    def __init__(self):
        self.parent = tk.Tk()
        # Car labelframe
        self.carLabelframe = ttk.Labelframe(master=self.parent, text="Add a Car")
        self.carLabelframe.grid(row=0, column=0, padx=5, pady=5, ipady=5, ipadx=5)
        self.trash = []
        # Name
        self.nameLabel = ttk.Label(master=self.carLabelframe, text="Name:")
        self.nameLabel.grid(row=0, column=7, rowspan=2)

        self.nameEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.nameEntry.grid(row=0, column=8, rowspan=2)
        # Make
        self.makeLabel = ttk.Label(master=self.carLabelframe, text="Make:")
        self.makeLabel.grid(row=0, column=0)

        self.makeEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.makeEntry.grid(row=0, column=1)
        # Model
        self.modelLabel = ttk.Label(master=self.carLabelframe, text="Model:")
        self.modelLabel.grid(row=0, column=2)

        self.modelEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.modelEntry.grid(row=0, column=3)
        # Year
        self.yearLabel = ttk.Label(master=self.carLabelframe, text="Year:")
        self.yearLabel.grid(row=0, column=4)

        self.yearEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.yearEntry.grid(row=0, column=5)
        # Odometer
        self.odoLabel = ttk.Label(master=self.carLabelframe, text="Odometer:")
        self.odoLabel.grid(row=1, column=0)

        self.odoEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.odoEntry.grid(row=1, column=1)
        # Colour
        self.colLabel = ttk.Label(master=self.carLabelframe, text="Colour:")
        self.colLabel.grid(row=1, column=2)

        self.colEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.colEntry.grid(row=1, column=3)
        # Price
        self.priceLabel = ttk.Label(master=self.carLabelframe, text="Price:")
        self.priceLabel.grid(row=1, column=4)

        self.priceEntry = tk.Entry(master=self.carLabelframe, width=12)
        self.priceEntry.grid(row=1, column=5)
        # Button to reset
        self.resetButton = ttk.Button(master=self.carLabelframe, text="Reset", command=self.reset)
        self.resetButton.grid(row=0, column=6, sticky=tk.E + tk.W, padx=5)
        # Button to add
        self.addButton = ttk.Button(master=self.carLabelframe, text="Add Car", command=self.createCar)
        self.addButton.grid(row=1, column=6, sticky=tk.E + tk.W, padx=5)

        # List of cars Labelframe
        self.listLabelframe = ttk.Labelframe(master=self.parent, text="Car Settings")
        self.listLabelframe.grid(row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=tk.E + tk.W + tk.N + tk.S)

        # Car combobox
        self.listBox = ttk.Combobox(master=self.listLabelframe, state="readonly", width=40)
        self.listBox.grid(row=0, column=0, columnspan=2, padx=5)

        # Delete a car button
        self.deleteButton = ttk.Button(master=self.listLabelframe, text="Delete Selected Car", command=self.deleteCar)
        self.deleteButton.grid(row=1, column=1, padx=5)

        #Check a car button
        self.checkButton = ttk.Button(master=self.listLabelframe, text="Check Selected Car", command=self.checkCar)
        self.checkButton.grid(row=1, column=0, padx=5)

        self.a = ttk.Label(master=self.listLabelframe,
                           text="Make: {}".format(" "))
        self.b = ttk.Label(master=self.listLabelframe,
                           text="Model: {}".format(" "))
        self.c = ttk.Label(master=self.listLabelframe,
                           text="Year: {}".format(" "))
        self.d = ttk.Label(master=self.listLabelframe,
                           text="Odometer: {}".format(" "))
        self.e = ttk.Label(master=self.listLabelframe,
                           text="Colour: {}".format(" "))
        self.f = ttk.Label(master=self.listLabelframe,
                           text="Price: {}".format(" "))

        self.a.grid(row=0, column=3, sticky=tk.E + tk.W, padx=14)
        self.b.grid(row=0, column=4, sticky=tk.E + tk.W, padx=14)
        self.c.grid(row=0, column=5, sticky=tk.E + tk.W, padx=14)
        self.d.grid(row=1, column=3, sticky=tk.E + tk.W, padx=14)
        self.e.grid(row=1, column=4, sticky=tk.E + tk.W, padx=14)
        self.f.grid(row=1, column=5, sticky=tk.E + tk.W, padx=14)

        # Customer labelframe
        self.customerLabelFrame = ttk.LabelFrame(master=self.parent, text="Customer Details")
        self.customerLabelFrame.grid(row=0, column=1, rowspan=2, sticky=tk.E + tk.W + tk.N + tk.S, padx=5, pady=5, ipadx=5, ipady=5)

        self.customerLabel = ttk.Label(master=self.customerLabelFrame, text="Customer Name: ")
        self.customerLabel.grid(row=0, column=0)

        self.customerEntry = ttk.Entry(master=self.customerLabelFrame, width=12)
        self.customerEntry.grid(row=0, column=1, pady=3)

        self.customerLabelPhone = ttk.Label(master=self.customerLabelFrame, text="Phone Number: ")
        self.customerLabelPhone.grid(row=1, column=0)

        self.customerPhoneEntry = ttk.Entry(master=self.customerLabelFrame, width=12)
        self.customerPhoneEntry.grid(row=1, column=1)

        self.maxBuy = ttk.Entry(master=self.customerLabelFrame, width=12)
        self.maxBuy.grid(row=2, column=1, pady=3)

        self.buyLabel = ttk.Label(master=self.customerLabelFrame, text="Maximum Budget")
        self.buyLabel.grid(row=2, column=0, pady=3)

        self.checkCustomer = ttk.Button(master=self.customerLabelFrame, width=10, text="Check", command=self.check)
        self.checkCustomer.grid(row=4, column=0, columnspan=2)

    def reset(self):
        #debugging
        print(self.makeEntry.get())
        print(self.listBox.current())
        print(self.trash[self.listBox.current()] == self.trash[0])
        #actual stuff
        self.makeEntry.delete(0, 'end')
        self.modelEntry.delete(0, 'end')
        self.yearEntry.delete(0, 'end')
        self.odoEntry.delete(0, 'end')
        self.colEntry.delete(0, 'end')
        self.priceEntry.delete(0, 'end')
        self.nameEntry.delete(0, 'end')

    def createCar(self):
        try:
            int(self.yearEntry.get())
            int(self.priceEntry.get())
        except ValueError:
            print("Invalid data type in one of the fields! (Either the year or the price)")
            return
        self.trash.append(Car(self.nameEntry.get(), self.makeEntry.get(), self.modelEntry.get(), self.yearEntry.get(),
                              self.odoEntry.get(), self.colEntry.get(), self.priceEntry.get()))

        self.listBox['values'] = self.trash
        self.reset()

    def deleteCar(self):
        self.trash[self.listBox.current()].deleteCar()
        del self.trash[self.listBox.current()]
        self.listBox['values'] = self.trash
        self.listBox.configure(state="normal")
        self.listBox.delete(0, 'end')
        self.listBox.configure(state='readonly')

    def checkCar(self):
        self.a = ttk.Label(master=self.listLabelframe, text="Make: {}".format(self.trash[self.listBox.current()].Script[0]))
        self.b = ttk.Label(master=self.listLabelframe, text="Model: {}".format(self.trash[self.listBox.current()].Script[1]))
        self.c = ttk.Label(master=self.listLabelframe, text="Year: {}".format(self.trash[self.listBox.current()].Script[2]))
        self.d = ttk.Label(master=self.listLabelframe, text="Odometer: {}".format(self.trash[self.listBox.current()].Script[3]))
        self.e = ttk.Label(master=self.listLabelframe, text="Colour: {}".format(self.trash[self.listBox.current()].Script[4]))
        self.f = ttk.Label(master=self.listLabelframe, text="Price: {}".format(self.trash[self.listBox.current()].Script[5]))

        self.a.grid(row=0, column=3, sticky=tk.E + tk.W, padx=10)
        self.b.grid(row=0, column=4, sticky=tk.E + tk.W, padx=10)
        self.c.grid(row=0, column=5, sticky=tk.E + tk.W, padx=10)
        self.d.grid(row=1, column=3, sticky=tk.E + tk.W, padx=10)
        self.e.grid(row=1, column=4, sticky=tk.E + tk.W, padx=10)
        self.f.grid(row=1, column=5, sticky=tk.E + tk.W, padx=10)

    def check(self):
        d = 0
        temp = []
        for i in self.trash:
            if self.maxBuy.get() >= i.Script[5]:
                temp.append(i.name)

        test=ttk.Label(master=self.customerLabelFrame, text="Available: {}".format(temp))
        test.grid(row=5, column=0, columnspan=50, sticky=tk.W)



a = Parent()
tk.mainloop()