class Employee:
    language = "Python"  #This is the class attribute.
    salary = 00000

    def __init__(self,name,salary,language):    #dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning.")

amin = Employee("Aminur",5000,"Javascript")
# amin.name = "Aminur"
print(amin.name,amin.salary,amin.language)