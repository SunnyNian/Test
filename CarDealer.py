
class Car:
    
    a = []
    b = []
    
    def __init__(self, Make, Model, Year, Odometer, Colour, Price):
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
        if Price is not int and Price is not float:
            print("The price should be a float.")
            return

        self.Script = [Make, Model, Year, Odometer, Colour, Price]
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
        return "Brand: {}\nModel: {}\nYear: {}\nOdometer: {}\nColour: {}\nPrice: {}\n".format(
                self.Script[0], self.Script[1], self.Script[2], self.Script[3], self.Script[4], self.Script[5])

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


# TO USE:
# 1. Set a car as a variable (e.g '''a = Car("make", "model", "year", "odometer", "colour", "price")
# 2. Different cars will be stored in Car.a, whereas the count of each car is stored in Car.b
# 3. To find a car already stored, run the command Car.findCar(make, model, year, odometer, colour, price")
# 4. To find out what a customer can purchase, run the command Car.customer(name, phone, income)
