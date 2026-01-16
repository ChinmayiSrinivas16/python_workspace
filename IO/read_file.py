with open("data1.txt", "w") as file:
    file.write("Hello File111")

with open("data1.txt", "r") as file:
    content = file.read()
    print(content)

file=open("data1.txt", "r")
content=file.read()
print(content)
file.close()