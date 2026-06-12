# file = open("File Handling\sample.txt", "a")

# # file.write("200 yEARS AGO")   # OVERWRITES THE ENTIRE FILE ('w')

# file.write("\n200 years after")  #adds to the file

# file.close()


# ---------------------------------------------------------------

text_data = "I like Pink"

text_path = "test_file.txt"

with open(text_path, "a") as file:
    file.write(text_data)

    