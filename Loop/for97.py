# Finding the average grade with list loop 

semester_grades = [4, 6, 3, 8 , 10]

passed = 0 
sum_grades = 0
for grades in semester_grades:
    if grades >= 5:
        passed += 1
        sum_grades += grades

print('You succed in ' + str(passed) + ' lessons')
print('The average is ' + str(sum_grades / passed))

# maybe i should try this again

