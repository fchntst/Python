# both condition must be true 

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan ')

else: 
    print('Ineligible for loan')

print('-------------------------')

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan ')

else: 
    print('Ineligible for loan')

print('-------------------------')

# at least on condition must be true

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print('Eligible for loan ')

else: 
    print('Ineligible for loan')

print('--------------------------------')

# and last but not least 
# not : inverse beelean value

has_criminal_records = True
has_good_credit = True

if has_good_credit and not has_criminal_records:
    print('Eligible for loan ')

else: 
    print('Ineligible for loan')