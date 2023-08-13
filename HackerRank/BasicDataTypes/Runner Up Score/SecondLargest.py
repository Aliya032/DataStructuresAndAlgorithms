# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     largest = max(arr)
#     i = 0
#     sec_largest = arr[1]
#     while i < len(arr):
#         if arr[i] > sec_largest and arr[i] < largest:
#             sec_largest = arr[i]
#         i = i+ 1
#     print(sec_largest)

#############################

# # taking number of input from users
# n = int(input('Enter the number of values: '))

# # taking the input and using the map function 
# lst = list(map(int, input('Enter numbers with spaces: ').strip().split()))[:n]

# #printing the output
# print('The final list is:', lst)

# list2 = list(set(lst))
# print('the list2 is: ', list2)

# list2.sort()
# print('Second largest element is: ', list2[-2])

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().strip().split()))[:n]
    list2 = list(set(lst))
    list2.sort()
    print(list2[-2])

# import sys

# if __name__ == '__main__':
#     n = int(input())
#     lst = list(map(int, input().strip().split()))[:n]
#     list2 = list(set(lst))
#     list2.sort()
#     print(list2[-2])