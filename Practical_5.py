'''Student name: Shelin Vankawala
Student Id: 20CS101
Practical 5 : You are given a string and your task is to swap cases. In other words, convert
all lowercase letters to uppercase letters and vice versa.
Sample Input: HackerRank.com presents "Pythonist 2".
Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".'''

n = input()
s = ''
for ch in n:
    if(ch.isupper() == True):
        s += (ch.lower())
    elif(ch.islower() == True):
        s += (ch.upper())
    else:
        s += ch
print(s)
