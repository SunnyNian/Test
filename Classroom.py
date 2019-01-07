import random

class Classroom:
    """
    This is a list of all classes, as well as the people registered in each class.
    """
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
        """

        :return:
        """

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

    @staticmethod
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

    def addclass(self, classname):
        if classname in Classroom.tenclass:
            for i in tenclass:
                if classname in i:
                    self.classes.append(i)
        if classname in Classroom.eleclass:
            for i in eleclass:
                if classname in i:
                    self.classes.append(i)
        if classname in Classroom.tweclass:
            for i in tweclass:
                if classname in i:
                    self.classes.append(i)

    def __str__(self):
        return "Name: " + str(self.surname) + ", " + str(self.name) + "\nYear of Birth: " + str(self.dob) + "\nAdministration Number: " + str(self.admin) +"\nClasses Enrolled: " + str(self.classes)

students = []
while True:
    choose = input("\n\n\n\n\n\n\n\n\n\n\nChoose an action:\n1) Add a student\n2) Enroll a student\n"
                   "3) View a Student's Details\n4)Add a class to a student\n5)Search a Class\n6) Quit")
    if choose == "1":
        students.append("Placeholder")
        name = input("\n\n\n\n\n\n\n\n\n\n\nEnter student's name:")
        last = input("\n\n\n\n\n\n\n\n\n\n\nEnter student's last name:")
        year = input("\n\n\n\n\n\n\n\n\n\n\nEnter student's year of birth:")
        if int(year) in [2001, 2002, 2003]:
            admi = input("\n\n\n\n\n\n\n\n\n\n\nEnter student's administrative number:")
            students[len(students) - 1] = Classroom(name, last, int(year), admi)
        else:
            input("Invalid year of birth!")

    elif choose == "2":
        firstname = input("\n\n\n\n\n\n\n\n\n\n\nStudent's first name?")
        lastname = input("\n\n\n\n\n\n\n\n\n\n\nStudent's last name?")
        for i, j in enumerate(students, 1):
            if firstname.upper() == j.name.upper() and lastname.upper() == j.surname.upper():
                j.enrollment()
                input("\n\n\n\n\n\n\n\n\n\n\nStudent enrolled!")
                break

    elif choose == "3":
        firstname = input("\n\n\n\n\n\n\n\n\n\n\nStudent's first name?")
        lastname = input("\n\n\n\n\n\n\n\n\n\n\nStudent's last name?")
        for i, j in enumerate(students, 1):
            if firstname.upper() == j.name.upper() and lastname.upper() == j.surname.upper():
                print(j)
                input()
                break

    elif choose == "4":
        breakthrough = False
        j = 0
        firstname = input("\n\n\n\n\n\n\n\n\n\n\nStudent's first name?")
        lastname = input("\n\n\n\n\n\n\n\n\n\n\nStudent's last name?")
        for i in students:
            if firstname.upper() == i.name.upper() and lastname.upper() == i.surname.upper():
                studentindex = j
                break
            j += 1

        while breakthrough is False:
            classname = input("\n\n\n\n\n\n\n\n\n\n\nWhat class would you like to add (Case sensitive!)?\n(Type 10, 11, or 12 to view different grade classes, Exit to quit)")
            try:
                if int(classname) == 10:
                    print(Classroom.tenclass)
                    input()
                elif int(classname) == 11:
                    print(Classroom.eleclass)
                    input()
                elif int(classname) == 12:
                    print(Classroom.tweclass)
                    input()
            except ValueError:
                if classname == "Exit":
                    break

                for i in Classroom.tenclass:
                    if classname in i:
                        students[studentindex].classes.append(i)
                        breakthrough = True
                        input("Success!")
                        break
                for i in Classroom.eleclass:
                    if classname in i:
                        students[studentindex].classes.append(i)
                        breakthrough = True
                        input("Success!")
                        break
                for i in Classroom.tweclass:
                    if classname in i:
                        students[studentindex].classes.append(i)
                        breakthrough = True
                        input("Success!")
                        break

    elif choose == "5":
        breakthrough = False
        while breakthrough is False:
            classname = input("\n\n\n\n\n\n\n\n\n\n\nWhat class would you like to search (Case sensitive!)?\n(Type 10, 11, or 12 to view different grade classes, Exit to quit)")
            try:
                if int(classname) == 10:
                    print(Classroom.tenclass)
                    input()
                elif int(classname) == 11:
                    print(Classroom.eleclass)
                    input()
                elif int(classname) == 12:
                    print(Classroom.tweclass)
                    input()
            except:
                try:
                    Classroom.search(classname)
                    input()
                    breakthrough = True
                except:
                    pass



    elif choose == "6":
        break
