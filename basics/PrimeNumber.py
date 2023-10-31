num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to num/2
    for i in range(2, int(num / 2) + 1):
        # If nm is divisible by any number between 2 and num/2, its not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number. ")
