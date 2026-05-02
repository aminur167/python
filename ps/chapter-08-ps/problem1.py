def greatest(a,b,c):
    if(a>b and a>c):
        return a;
    elif(b>a and b>c):
        return b;
    elif(c>a and c>b):
        return c;
a = int(input("Enter the value of a:"));
b = int(input("Enter the value of b:"));
c = int(input("Enter the value of c:"));

print(greatest(a,b,c));