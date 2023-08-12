# Using map to take the input as a list

#number of elements
n = int(input('Enter the number of elements:'))

# reads input form the user using map() function 
a = list(map(int, input('\nEnter the numbers (with spaces): '). strip().split()))[:n]

print('\n List is: ', a)