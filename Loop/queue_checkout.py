# A queue at the checkout = μία ούρα στο ταμείο

cash_desk = []
cash_desk.append('Tom')
cash_desk.append('Bob')
print(cash_desk)

person = cash_desk.pop(0)
print(person + ' served.')

cash_desk.extend(["Pam", "Jim"])
print(cash_desk)

person2 = cash_desk.pop(0)
print(person2 + ' served.')
print(cash_desk)
