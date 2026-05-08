x = 10

def change():
    global x
    x = 20
    print("Inside function:", x)

change()

print("Outside function:", x)   