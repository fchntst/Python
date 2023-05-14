from random import seed  # seed = σπορος
from random import randrange
from datetime import datetime # all 3 at the beginning

N = 10

pupils = set()
for number in range(N):
    pupils.add("pupil " + str(number))

list_pupils = list(pupils)
math_teams = set()
for _ in range(N // 2):
    pos1 = randrange(0, len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    math_teams.add(team)
print("math_teams: " + str(math_teams))

list_pupils = list(pupils)
geography_teams = set()
for _ in range(N // 2):
    pos1 = randr222222222222222222222222222222ange(0, len(list_pupils))
    pupil1 = list_pupils.pop(pos1)
    pos2 = randrange(0, len(list_pupils))
    pupil2 = list_pupils.pop(pos2)
    team = (pupil1, pupil2)
    geography_teams.add(team)

print("geography_teams: " + str(geography_teams))