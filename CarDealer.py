
class Car:
    
    a = []
    b = []
    
    def __init__(self, Make, Model, Year, Odometer, Colour, Price):
        self.Script = [Make, Model, Year, Odometer, Colour, Price]
        self.condense()
        
    def condense(self):
        
        if self.Script not in Car.a:
            Car.a.append(self.Script)
            Car.b.append(1)
        else:
            for i in Car.a:
                if self.Script == i:
                    Car.b[Car.a.index(i)] = Car.b[Car.a.index(i)] + 1
                    break
                
    def __str__(self):
        return "Brand: {}\nModel: {}\nYear: {}\nOdometer: {}\nColour: {}\nPrice: {}\n".format(
                self.Script[0], self.Script[1], self.Script[2], self.Script[3], self.Script[4], self.Script[5])

    @staticmethod
    def findCar(Make, Model, Year, Odometer, Colour, Price):
        carType = [Make, Model, Year, Odometer, Colour, Price]
        for i in Car.a:
            if carType == i:
                car = Car.b[Car.a.index(carType)]
                print("Car found!\nCar Characterstics:\nBrand: {}\nModel: {}\nYear: {}\nOdometer: {}\nColour: {}\nPrice: {}".format(Make, Model, Year, Odometer, Colour, Price))
                print("\nNumber available: {}".format(car))
                break
        print("Search for car has ended.")

    @staticmethod
    def customer(name, phone, income):
        print("Searching for cars for {} ({})\n".format(name, phone))
        for i in Car.a:
            if i[5] <= income:
                print("Car {}:\nBrand: {}\nModel: {}\nYear: {}\nOdometer: {}\nColour: {}\nPrice: {}\n________________________\n".format(Car.a.index(i), i[0], i[1], i[2], i[3], i[4], i[5]))

        print("Search for car has ended.")


# TO USE:
# 1. Set a car as a variable (e.g '''a = Car("make", "model", "year", "odometer", "colour", "price")
# 2. Different cars will be stored in Car.a, whereas the count of each car is stored in Car.b
# 3. To find a car already stored, run the command Car.findCar(make, model, year, odometer, colour, price")
# 4. To find out what a customer can purchase, run the command Car.customer(name, phone, income)
