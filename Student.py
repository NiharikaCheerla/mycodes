class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def showdetails(self):
        print(f"Name:self.name, Age:self.age, Gpa:self.gpa")
    
Student1 = Student('niha', 29, 3.4)
Student2 = Student('priya', 27, 3.9)
Student3 = Student('sriram', 23, 4)

Student1.showdetails()
Student2.showdetails()
Student3.showdetails()
            