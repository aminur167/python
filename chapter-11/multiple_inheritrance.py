class Employee:
    name = "Default name"
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}.")

class Coder:
    language = "Javascript"
    def printLanguage(self):
        print(f"Out of all the languages here is your language : {self.language}")


class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")



a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
