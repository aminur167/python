a = int(input("Enter your age: "))
if a >= 18:
    print("You are an adult.")  
elif a<0:
    print("Invalid age.")
elif a==0:
    print("You are a newborn.")
else:
    print("You are a minor.")  
print("End of program. ")