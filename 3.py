grades = [[8, 10, 6], [7, 5, 8], [6,7,8]]
averages = []
for student in grades:
    sum = 0
    for i, grade in enumerate(student):
        sum += grade
        if i == len(student) - 1:
            average = sum / len(student)
            averages.append(average)
            sum = 0
    
print(f"averages: {averages}")
generalAverage = 0
sum = 0
for average in averages:
    sum += average

generalAverage = sum / len(averages)
print(f"general average {generalAverage}")