# taking number of input from users
n = int(input('Enter the number of values: '))

# taking the input and using the map function 
lst = list(map(int, input('Enter numbers with spaces: ').strip().split()))[:n]

#printing the output
print('The final list is:', lst)

def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x

    return max

print("the max element is: ", myMax(lst))
## Time Complexity: O(n)
## Auxilary space: O(1)