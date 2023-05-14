from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

n = 10  # let's suppose the number of the students is 10 

students = set()

for student in range(n + 1):
    students.add("pupil " + str(student)) 


list_sutdents = list(students)
math_team = set()

for student in range(n // 2):
    math_student1 = randrange(0, len(list_sutdents))
    math_pupil1 = list_sutdents.pop(math_student1)
    math_student2 = randrange(0, len(list_sutdents))
    math_pupil2 = list_sutdents.pop(math_student2)
    team1 = (math_pupil1, math_pupil2)
    math_team.add(team1)

print("math team: " + str(math_team))

list_sutdents = list(students)
geography_team = set()

for student in range(n // 2):
    math_student1 = randrange(0, len(list_sutdents))
    math_pupil1 = list_sutdents.pop(math_student1)
    math_student2 = randrange(0, len(list_sutdents))
    math_pupil2 = list_sutdents.pop(math_student2)
    team1 = (math_pupil1, math_pupil2)
    geography_team.add(team1)

print("geography team: " + str(geography_team))
