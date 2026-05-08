try:
    a = int(input("Enter the number: "))

    if a < 0:
        raise ValueError("Negative number is not allowed!")

    print(a)

except Exception as e:
    print(e)