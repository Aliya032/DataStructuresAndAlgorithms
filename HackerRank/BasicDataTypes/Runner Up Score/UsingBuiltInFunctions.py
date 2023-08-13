# number of elements
n = int(input('Number of elements:'))

# # appendint them to the list
# lst = []
# for i in range(0, n):
#     ele = int(input('Enter the numbers: '))
#     lst.append(ele)
# print('Here\' the final list',lst)

# reads input form the user using map() function 
a = list(map(int, input('\nEnter the numbers (with spaces): '). strip().split()))[:n]

print('\n List is: ', a)
list.sort(a)
print('Second Larget Element Is: ', a[-2])