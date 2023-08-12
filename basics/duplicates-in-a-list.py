# number of elements
n = int(input('Number of elements:'))

# appendint them to the list
lst = []
for i in range(0, n):
    ele = int(input('Enter the numbers: '))
    lst.append(ele)
print('Here\' the final list',lst)

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            print(str(lst[i]) + " is a duplicate")
            break

## Time complexity is a*n^2 + b -> O(n^2)