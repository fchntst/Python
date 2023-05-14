dictionary = {

}

name = str(input('give a name: '))
dictionary['name'] = name

surname = str(input('give a surname: '))
dictionary['surname'] = surname

fathers_name = str(input("Give a father's name: "))
dictionary["father's name"] = fathers_name 

date_birth = input('Give a date birth: ')
dictionary['date birth'] = date_birth

adress = input('give adress: ')
dictionary['adress'] = adress

phone_number = int(input('give a phone number: '))
dictionary['phone number'] = phone_number


print('ανοματεπωνυμο  :' + ' ' + dictionary['name'] + " " + dictionary['surname'] + " " + dictionary["father's name"])
print('Ημ/νια Γεννησης:' + " " + dictionary['date birth'])
print('διευθηνση      :' + " " + dictionary['adress'])
print('τηλεφωνο       :' + " " + str(dictionary['phone number']))
