## Method 2 for taking input from users 

try:
    my_list = []

    while True:
        my_list.append(int(input()))

## if the input is not an integer, just print the list
except:
    print(my_list)