class Employee:
    name = "Aminur"    #This is a class attribute.
    language = "python"
    salary = 0000

amin = Employee()

amin.name = "Aminur Islam"  #This is an instance attribute.
print(amin.name,amin.language,amin.salary)


momin = Employee()
momin.name = "Abdul Momin"
print(momin.name,momin.language,momin.salary)
