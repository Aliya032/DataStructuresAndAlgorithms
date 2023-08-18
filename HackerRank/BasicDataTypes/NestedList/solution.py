# take value of n
no_of_students = int(input())

# creating an emtpy list
records = []

# appending record of each student name,score in a for loop
for i in range(no_of_students):
    name = input()
    score = float(input())
    records.append([name, score])

# converting into a dictionary
records = dict(records)

# get only values from our dictionary and using set function to remove any duplicate scores
scores = sorted(set(records.values()))

# index 1 has the second lowest score
second_lowest_score = scores[-2]

# creating a list of names of students who has the 2nd lowest score using list comprehensions
second_lowest_students = [name for name,score in records.items() if score == second_lowest_score]


#sorting the student names in alphabetical order
second_lowest_students.sort()

# # loop through each name and print
for name in second_lowest_students:
    print(name)