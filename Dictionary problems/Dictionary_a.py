'''Student name : Shelin Vankawala 
Student Id : 20CS101
Practical 2 - Dictionary 
Aim a : Write a Python script to check whether a given key already exists in a dictionary.'''
Person = {'Rohit': '1', 'Siya': '2',
          'Jessica': '3', 'Aditi': '4', 'Darshiv': '5'}


def key(x):
    if x in Person:
        print(x, "is present.")
    else:
        print(x, "is not present.")


key('Aditi')
key('Arnav')
