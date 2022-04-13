'''Student name: Shelin Vankawala
Student Id: 20CS101
Practical 3 : Find Captain Room Number
    Sample Input
    5
    1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
    Sample Output
    8'''


counts = {}
n = input()
number = input().split()
for i in number:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] = counts[i] + 1

for i in counts:
    if counts[i] == 1:
        print(i)
