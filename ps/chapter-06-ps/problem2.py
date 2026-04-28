mark1 = int(input("Enter the marks 1: "))
mark2 = int(input("Enter the marks 2: "))
mark3 = int(input("Enter the marks 3: "))

# check for total percentage
total_percentage = (mark1 + mark2 + mark3) / 3 
   
if (total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("Congratulations! You have passed the exam.",total_percentage)
else:
    print("Sorry! You have failed the exam.",total_percentage)