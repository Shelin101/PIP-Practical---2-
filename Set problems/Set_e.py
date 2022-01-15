'''Student name : Shelin Vankawala 
Student Id : 20CS101
Practical 2 - Set
Aim e : Write a Python program to find the most common elements and their counts from list, tuple, dictionary.'''

from collections import Counter
dict1 = {1: 2, 2: 8, 3: 4, 4: 8, 5: 8}
tuple1 = (2, 4, 2, 3, 1, 2, 8, 90)
list1 = [2, 5, 6, 11, 9, 23, 5, 2, 3, 11, 5]

# To count most common element and its count for Dictionary
frequency = {}
for value in dict1.values():
    if value in frequency:
        frequency[value] = frequency[value] + 1
    else:
        frequency[value] = 1
print("Dictionary most common element : ", frequency[value])
print("Counts : ", value)

# To count most common element and its count for Tuple
b = Counter(tuple1)
print("Most frequent element of tuple and its count : ", b.most_common(1))

# To count most common element and its count for List
counter = 0
num = list1[0]

for i in list1:
    x = list1.count(i)
    if(x > counter):
        counter = x
        num = i

print("List most common element : ", num)
print("Counts : ", counter)
