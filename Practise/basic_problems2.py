# Problem 1 — Word Frequency + Sorting (Dict + List + Loop)

# Given a paragraph, find the top 3 most frequent words.
# Steps:

# Convert paragraph into list of words

# Build frequency dictionary

# Convert dictionary into (word, count) tuples

# Sort them in descending order

# Print top 3

# Concepts used: split(), dict, loops, sorting, list of tuples

# para = "pogi hajima dno h
#     if word in dic:
#         dic[word] += 1
#     else:
#         dic[word] = 1

# for word in range(3):
#     max_key = 0
#     max_value = 0
#     for key,value in dic.items():
#         if key not in maxii and value > max_value:
#             max_value = value
#             max_key = key
#     top3.append((max_key,max_value))
#     maxii.append(max_key)
# print(top3)
    




# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(64+i),end=" ")
#     print()

n = 4
for i in range(1,n+1):
    count = 2
    for j in range(i):
        print(count,end=" ")
        count += 2
    print()