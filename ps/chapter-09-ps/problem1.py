def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"ps/chapter-09-ps/tables/table_{n}", "w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)