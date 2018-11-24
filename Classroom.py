import random

class Classroom:

    tencount = [[],[],[],[],[],[],[],[],[],[]]
    elecount = [[], [], [], [], [], [], [], [], [], [], []]
    twecount = [[], [], [], [], [], [], [], [], [], [], []]

    tenclass = [["Math 10-1", "MT1010"], ["Math 20-1", "MT1020"],
                ["Science 10-1", "SC1010"], ["Social Studies 10-1", "SO1010"],
                ["English 10-1", "EN1010"], ["Computing Science 10-1", "CS1010"],
                ["Physical Education 10", "PE1010"], ["Band 10", "BA1010"],
                ["Speech & Debate 10", "SD1010"], ["Drama 10", "DR1010"]]

    eleclass = [["Math 30-1", "MT1130"], ["English 20-1", "EN1120"],
                ["Social Studies 20-1", "SO1120"],
                ["Computing Science 20-1", "CS1120"], ["Physical Education 20", "PE1120"],
                ["Band 20", "BA1120"], ["Speech & Debate 20", "SD1120"],
                ["Drama 20", "DR1120"], ["Physics 20-1", "PH1120"], ["Biology 20-1", "BI1120"],
                ["Chemistry 20-1", "CH1120"]]

    tweclass = [["Math 31", "MT1231"],
                ["Social Studies 30-1", "SO1230"], ["English 30-1", "EN1230"],
                ["Computing Science 30-1", "CS1230"], ["Physical Education 30", "PE1230"],
                ["Band 30", "BA1230"], ["Speech & Debate 30", "SD1230"],
                ["Drama 30", "DR1230"], ["Physics 30-1", "PH1230"], ["Biology 30-1", "BI1230"],
                ["Chemistry 30-1", "CH1230"]]

    def __init__(self, name, surname, year, admin):
        #initializer
        self.name = name
        self.surname = surname
        self.dob = year
        self.admin = admin
        self.classes = []

    def enrollment(self):
        #list of classes

        tenoption = random.randint(5, 9)
        eleoption = random.randint(4, 8)
        sciences = random.randint(8, 10)

        t = 0

        global tencount
        global elecount
        global twecount
        global tenclass
        global eleclass
        global tweclass

        if 2018 - self.dob == 15:
            for i in range(5):
                self.classes.append(Classroom.tenclass[i])
                Classroom.tencount[i].append([self.name, self.surname, self.admin])
            self.classes.append(Classroom.tenclass[tenoption])
            Classroom.tencount[tenoption].append([self.name, self.surname, self.admin])

        elif 2018 - self.dob == 16:
            for i in range(3):
                self.classes.append(Classroom.eleclass[i])
                Classroom.elecount[i].append([self.name, self.surname, self.admin])
            for i in range(2):
                while t < 2 :
                    sciences = random.randint(8, 10)
                    if Classroom.eleclass[sciences] not in self.classes:
                        self.classes.append(Classroom.eleclass[sciences])
                        Classroom.elecount[sciences].append([self.name, self.surname, self.admin])
                        t = t + 1
            self.classes.append(Classroom.eleclass[eleoption])
            Classroom.elecount[eleoption].append([self.name, self.surname, self.admin])

        elif 2018 - self.dob == 17:
            for i in range(3):
                self.classes.append(Classroom.tweclass[i])
                Classroom.twecount[i].append([self.name, self.surname, self.admin])
            for i in range(2):
                while t < 2:
                    sciences = random.randint(8, 10)
                    if Classroom.tweclass[sciences] not in self.classes:
                        self.classes.append(Classroom.tweclass[sciences])
                        Classroom.twecount[sciences].append([self.name, self.surname, self.admin])
                        t = t + 1
            self.classes.append(Classroom.tweclass[eleoption])
            Classroom.twecount[eleoption].append([self.name, self.surname, self.admin])

    def search(classn):
        for i in range(len(Classroom.tenclass)):
            if classn in Classroom.tenclass[i]:
                print(str(Classroom.tencount[i]) + " in " + classn)
                return

        for i in range(len(Classroom.eleclass)):
            if classn in Classroom.eleclass[i]:
                print(str(Classroom.elecount[i]) + " in " + classn)
                return

        for i in range(len(Classroom.tweclass)):
            if classn in Classroom.tweclass[i]:
                print(str(Classroom.twecount[i]) + " in " + classn)
                return

    def __str__(self):
        return "Name: " + str(self.surname) + ", " + str(self.name) + "\nYear of Birth: " + str(self.dob) + "\nAdministration Number: " + str(self.admin) +"\nClasses Enrolled: " + str(self.classes)

#To use:
#Create a student as an object: a = Classroom("first name", "last name", birthyear, administration no.)
#Enroll the student in classes: a.enrollment()
#If you want to see details of the student: print(a)
#If you want to see every student in a class: Classroom.search("Math 31"), or Classroom.search("MT1231")