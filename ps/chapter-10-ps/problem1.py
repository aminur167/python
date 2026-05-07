class Programmer:
    company = "Google"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Aminur",5000,200000)
print(p.name,p.company,p.salary)
r = Programmer("Ridoy",3000,20367892)
print(r.name,r.company,r.salary)