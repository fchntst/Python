# print the cities in the list that are in evens positions

my_cities = ['New York', 'Athens', 'London', 'Paris', 'Rome']

for position in range(0,5+1,2):
    if position % 2 == 0:
        print(my_cities[position])


        
    