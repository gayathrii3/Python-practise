# Find the common elements between two sets.

# set1 = {1,2,3,4}
# set2 = {2,3,5,7,8}
# print(f"comman elements are :{set1.intersection(set2)}")

#-------------------------------------------------------------
# Check if a set is a subset of another set(both sets elements dhould match)

# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4}
# print(set1.issubset(set2))

#-------------------------------------------------------------
# Print all keys of a dictionary.

# dic = {"name" : "Gayathri",
#        "age" : 19,
#        "fav_movie" : "Magadheera",
#        "cartoon" : "Creep school"}
# print(dic.keys())

#-------------------------------------------------------------
# Add a new key–value pair to a dictionary.

# dic = {"name" : "Gayathri",
#        "age" : 19,
#        "fav_movie" : "Magadheera",
#        "cartoon" : "Creep school"}
# dic.update({"kite" : "pink"})
# print(dic.items())

#--------------------------------------------------------------
# Remove an element from a set without using remove() or discard()

# set = {"Gayathri","harry","BroCode","ApnaClg","Harikrit","Striver"}
# for name in list(set):
#     if name.startswith("G"):
#         set.remove(name)
# print(set)

#---------------------------------------------------------------
# Find elements present in list1 but not in list2 (using sets)

# list1 = set([1,2,3,4])
# list2 = set([9,2,4,3,0])

# new = list1.difference(list2)
# print(new)

#----------------------------------------------------------------
# Given a list of words, print words that appear more than once using sets.

# list = ["Heidi","Creepschool","Heidi","Jackiechan","Dragonball","Jackiechan"]
# set = set()
# for word in list:
#     if list.count(word) > 1:
#         set.add(word)
# print(set)

#---------------------------------------------------------------------
# Find the symmetric difference between two lists using sets (without using built-in method).

# list1 = [1,2,3,4]
# list2 = [2,4,5,6]

# set1 = set(list1)
# set2 = set(list2)
# diff = set()

# for n in set1:
#     if n not in set2:
#         diff.add(n)
# for x in set2:
#     if x not in set1:
#         diff.add(x)
# print(diff)
            
        