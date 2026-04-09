#Create a dictionary where names are keys and marks are value

# names = ["Asha", "Rahul", "Meena","o"]
# marks = [89, 76, 91,7]

# dict = {}
# for i in range(len(names)):
#     dict[names[i]] = marks[i]
# print(dict)

#--------------------------------------------------------------
#Count how many times each character appears in a string using a dictionary.

# word = 'Gayathri'
# dict = {}

# for ch in word:
#     if ch not in dict:
#         dict[ch] = 1
#     else:
#         dict[ch] += 1
# print(dict)

#-------------------------------------------------------------------
# Find the key with the highest value in a dictionary (without using max())

# cartoon = {"PowerRangers" : 6,
#            "Ben10" : 1,
#            "TeenTitanGo" : 4,
#            "Kiteresu" : 2}
# highest_value = -1
# highest_key = None

# for key,value in cartoon.items():
#     if value > highest_value:
#         highest_value = value
#         highest_key = key
# print(f"Highest value is {highest_value},key is {highest_key}")

#-----------------------------------------------------------------
# Find the key with the highest value in a dictionary (without using max()).

# marks = {"English" : 87,
#          "Maths" : 45,
#          "Science" : 91,
#          "Social" : 78,
#          "History" : 84}
# highest_value = -1
# highest_key = None

# for key,value in marks.items():
#     if value > highest_value:
#         highest_value = value
#         highest_key = key
# print(f"Highest key is {highest_key} and highest value is {highest_value} ")

#--------------------------------------------------------------------
    
# Swap the keys and values of a dictionary (make values the new keys).

# movies = {"Ramcharan" : "Magadheera",
#           "Prabhas" : "Darling",
#           "Kavin" : "Dada",
#           "Rishab Shetty" : "Kantara",}
# swapped = {value: key for key ,value in movies.items()}
# print(swapped)
    
#----------------------------------------------------------------------
# Merge two dictionaries manually (no update() function).

# Sonic = {"Power Rangers" : 1,
#          "Zig&Sharko" : 2,
#          "Dragon Ball" : 3,
#          "Anpanamn" : 4}
# KushiTV = {"JackieChan" : 5,
#            "Heidi" : 6,
#            "Heman" : 7,
#            "Stuart Little" : 8}
# merged = {}

# for key,value in Sonic.items():
#     merged[key] = Sonic[key]
#     for key,value in KushiTV.items():
#         merged[key] = KushiTV[key]
# print(merged)

#---------------------------------------------------------
# Print all keys that have duplicate values.

# movies = {"RamCharan" : "Yevadu","AlluArjun" : "Yevadu","Rishabshetty" : "Kaantara","Prabhas" : "Darling",}
# value_to_keys = {}
# for key, value in movies.items():
#     if value in value_to_keys:
#         value_to_keys[value].append(key)
#     else:
#         value_to_keys[value] = [key]
        
# for value, keys in value_to_keys.items():
#     if len(keys) > 1:
#         print(f"Keys with value '{value}': {keys}")

#-----------------------------------------------------------------------------------
# Create a dictionary to store values as keys and their corresponding keys as lists

# data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
# result = {}

# for key,value in data.items():
#     if value not in result:
#         result[value] = [key]
#     else:
#         result[value].append(key)
# print(result)
    
#-----------------------------------------------------------------------------------
# Iterate through the movies dictionary

# movies = {
#     "Inception": 2010,
#     "Interstellar": 2014,
#     "Dune": 2021,
#     "Avatar": 2009
# }
# for title in movies:
#     print(title)

#-------------------------------------------------------------------
# Print keys that share the same value

# data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
# same = {}
# for key,value in data.items():
#     if value not in same:
#         same[value] = [key]
#     else:
#         same[value].append(key)
# print(same)
    
#------------------------------------------------------------------
# Given a dictionary of student names and marks, print students who scored above 80.

# student = {"Jackie" : 67,
#            "Marie" : 84,
#            "Nancy" : 72,
#            "katie" : 81}

# for name,marks in student.items():
#     if marks > 80:
#         print(name,marks)
        
#-------------------------------------------------------------------
# Convert a list of tuples into a set of unique tuples.

# list = set([(2,3),(8,2),(2,3),(9,1)])
# print(list)
