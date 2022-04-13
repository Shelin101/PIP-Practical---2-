'''Student name: Shelin Vankawala
Student Id: 20CS101
Practical 4 : Find runner-up from given list
Sample Input
5
2 3 6 6 5
Sample Output
5'''

n = int(input())
A = map(int, input().split())
print(sorted(list(set(A)))[-2])
