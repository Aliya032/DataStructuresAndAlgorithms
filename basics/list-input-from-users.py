## taking input from users and making it as a list
lst = []

# number of elements as input
n = int(input('Enter the number of elements:'))

#iterating till the range
for i in range(0, n):
    ele = int(input())
    #adding element
    lst.append(ele)

print(lst)