# number of elements
n = int(input('Number of elements:'))

# appendint them to the list
lst = []
for i in range(0, n):
    ele = int(input('Enter the numbers: '))
    lst.append(ele)
print('Here\' the final list',lst)

to_search = int(input('Number to look for: '))

for i in range(len(lst)):
    if lst[i] == to_search:
        print('The number is at position ', str(i))

