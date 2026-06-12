file = open("File Handling\sample.txt", "r")

line1 = file.readline()
print(line1)

line2 = file.readline()
print(line2)
# ------------------------------------------------------
# data = file.read(50)
# print(data)
# print(type(data))

file.close()

# --------------------------------------------------------

with open("File Handling\sample.txt", "r") as file:
    content = file.read()
    print(content)

file.close()
