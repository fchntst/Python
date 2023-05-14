lexicon = {
    'ιταμος':'προκλητικος, αυθαδης, αναιδης',
    'ονειδος':'ντροπη, κατασχυνη',
    'πομφολυγες':'αερολογιες, ανοησιες',
}
print(lexicon)

lexicon['φληναφηματα'] = 'ανοησιες, σαχλαμαρες'
print(lexicon)

user_input = str(input('γραψε το κλειδι: '))
user_value = str(input('γραψε την τιμη: '))

lexicon[user_input] = user_value
print(lexicon)
