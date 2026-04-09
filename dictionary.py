# Create a dictionary from two lists: one list of keys, one list of values.

# list1 = ["Name","Age","Movie","Cartoon"]
# list2 = ["Gayathri",19,"Star","SpyXFamily"]

# dic = {}

# for i in range(len(list1)):
#     dic[list1[i]] = list2[i]               
# print(dic)
    
#------------------------------------------------------------------------
# Find the key with the maximum value in a dictionary.

# dic = {"english" : 89,
#        "hindi" : 99,
#        "maths" : 59,
#        "science" : 76}
# max_key = 0
# max_value = 0

# for key in dic:
#     if dic[key] > max_value:
#         max_value = dic[key]
#         max_key = key
# print(max_key,max_value)

#----------------------------------------------------------------------------
# In a dictionary of student marks, find the top 3 students.

# marks = {"Anish" : 34,
#          "haritha" : 97,
#          "mahitha" : 76,
#          "charitha" : 67,
#          "lalitha" :82}
# top3 = []
# jk = []

# for i in range(3):
#     max_key = 0
#     max_value = 0
#     for key,value in marks.items():
#          if key not in jk and value > max_value:
#              max_value = value
#              max_key = key
#     top3.append((max_key,max_value))
#     jk.append(max_key)
# print(top3)
        
#------------------------------------------------------------------------------
# Create a dictionary where key = word, value = frequency of that word in a paragraph.

# text = "I love coding and I love Python because coding is fun"

# words = text.split()
# dic = {}

# for word in words:
#     if word not in dic:
#         dic[word] = 1
#     else:
#         dic[word] += 1
# print(dic)