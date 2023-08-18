# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200, 2350, 2600, 2130]

print('How many dollars you spent extra compared to January?', exp[1]-exp[0])

# 2. Total expenses in first quarter of the year
first_quarter = exp[0] + exp[1]+ exp[2]
print(first_quarter)

# 3. Find out if you spend exactly 2000 dollars in any month

## Using 'in' Method
i = 2000
if i in exp:
    print('exist')
else:
    print('no not spent 2000')

# Using a loop
for z in exp:
    if z == 2130:
        print('Element found')
    else:
        print('Not found')

## Using the count()
exist_count = exp.count(2000)
if exist_count > 0:
    print("yes, element found")
else: 
    print('no its not there')


# 4. add june month expenses to the exisitng list
exp.append(1980)
print('exp new\n',exp)

## Using append()
new_list = ['apple', 'banana', 'mango', 'strawberr7']
new_list.append('guava')
print('using append()',new_list)

#using insert
new_list.insert(2, 'magic ')
print('using insert()', new_list)

# using extend()
anothe_list = ['wifey', 'dollar']
anothe_list.extend(new_list)
print('another list', anothe_list)

# 5. you returned an item that you bought in a months of April and got a refund of 200$. Make a correction to your monthy expense list based on this
exp[3] = exp[3] - 200
print('Expenses after 200$ return in april: ', exp``)