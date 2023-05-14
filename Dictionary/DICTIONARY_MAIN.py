# the left side of the colon is called key and the right called value pairs
# or aka key-value pairs

# the key can be only one time in a dictionary and not more than one
# the key is immutable we can't add there sets and lists 
# the values are mutable we can add there whatever the fuck we want
# in dictionaries there are not indexes and ranges cuse they don't make sense...

empty = {}

person = {
    'name': 'Tony',
    'weight': str(70) + "kg",
    (1,2): 17,
    'name1': 'alex',        # if we want we can put a comma at the last value
}                           # but this is iptional    
print(person)
print(type(person))
print('-------------------------------------------------------------------')
# another example
# alias btw stands for ψευδονυμο
individual = {
    'name': 'Tony Stark',
    'Alias': 'Iron man',
    'Power': 20,
} 
print(individual)
print('-------------------------------------------------------------------')

# access to an item 
# $ dict_name[key] or dict_name.get(key) $

# add an item to a dictionary
# $ dict_name[key] = value $

hero = {'name':'Bruce Banner', 'alias':'Iron man'}
print(hero)
hero['name'] = 'Tony Stark'
hero['equipment'] = 'suite'
print(hero)
print('-------------------------------------------------------------------')

hero1 = {
    'name':'Tony Stark',
    'alias':'Iron  man',
}

hero2 = hero1.copy()
hero2['equipment'] = 'suite'
print(hero2) 
print('-------------------------------------------------------------------')

# methods for subtracting values pairs from dict.
# $ dict_name.pop(key) $
# $ dict_name.popitem() $ it subtracts the last value pair
# $ dict_name.clear() $

# conversions in dict:
# $ dict_name = dict(collection) $ but with the prerequisite that the collection has only tuples 
# with two elements inside 

a_list = [('name', 'Natasha Romanoff'), ('alias', 'Black Widow')]
hero = dict(a_list)
hero['ability'] = 'hand-to-hand combat'
print(hero)
hero.pop('name')
print(hero)
hero.clear()
print(hero)

# repitition in dictionaries

# $ for key in dict $ 
# it goes across the keys

# $ for key, value in dict.items() $ 
# it goes across at the same time the key and the value

# $ for key in dict.keys() $
# it goes across the keys without sort

# $ for value in dict.values() $ 
# it goes across the values (with repititions)