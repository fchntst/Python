# age recongnizer  

age = int(input("type here your age: ")) 

if 0 < age < 18:
    print('you are underage')

elif 18 <= age <= 65:
    print('you are an adult')  

else:
    print('you are an elderly')
