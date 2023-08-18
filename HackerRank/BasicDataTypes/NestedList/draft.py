# take value of n
no_of_students = int(input())

#creating empty list
records = []

#append record of each student name,score in a for loop
for i in range(no_of_students):
    name = input()
    score = float(input())
    records.append([name, score])

# print('The records are: ', records)

# converting list of records into a python dictionary
records = dict(records)
# print(records)

# getting only values from our dictionary and using set function to remove scores then sort it in ascending order
scores = sorted(set(records.values()))

# print(scores)

# index 1 has the second lowest score
# second_lowest_score = scores[1]
second_lowest_score = scores[-2]
# print(second_lowest_score)

# #creating a list of names of students who has 2nd lowest score using list comprehensions
second_lowest_students = [name for name, score in records.items() if score == second_lowest_score]

# # # print(second_lowest_students)
second_lowest_students.sort()

# # # looping through each name and printing
for name in second_lowest_students:
    print(name)
