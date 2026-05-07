# f = open("chapter-09/file.txt","r")
# data = f.read()
# print(data)
# f.close()

# The same can be written using with statement like this : 
with open("chapter-09/file.txt") as f :
    print(f.read())