# word = "Aminur"

# with open("ps/chapter-09-ps/file.txt","r") as f:
#     content = f.read()

# contentNew = content.replace(word,"*****")

# with open ("ps/chapter-09-ps/file.txt","w") as f:
#     f.write(contentNew);


words = ["Aminur","python","full"]

with open("ps/chapter-09-ps/file.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open ("ps/chapter-09-ps/file.txt","w") as f:
    f.write(content);