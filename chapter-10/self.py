class Employee:
    name = "Aminur"    #This is a class attribute.
    language = "python"
    salary = 0000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}.")

amin = Employee()

amin.language = "javascript"  #This is an instance attribute.
# Employee.getInfo(amin)        or
amin.getInfo()
