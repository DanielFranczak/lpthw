# dicts lets me use anything not only numbers like in the lists, the dicts works like key:value
# create a mapping of voivedoship of state to abbreviation
voivedoships = {
    'Mazowieckie': 'Warszawa',
    'Malopolskie': ' Krakow',
    'Wielkopolskie': 'Poznan',
    'Kuj.-Pomorskie': 'Bydgoszcz',
    'Dolnoslaskie': 'Wroclaw'
}
# create a basic set of voivedoships and some cities in them
cities = {
    'Warszawa': 'Var',
    'Krakow': 'Cra',
    'Poznan': 'Pos'
}
# add some more cities
cities['Bydgoszcz'] = 'Bdg'
cities['Wroclaw'] = 'Wro'

#print out some cities
print('-' * 10)
print("Mazowieckie voivedoship has: ", voivedoships['Mazowieckie'])
print("Malopolskie voivedoship has:", voivedoships['Malopolskie'])

#print out some voivedoships

print('-'*10)
print('Warszawa\'s abbreviation is:', cities['Warszawa'])
print('Krakow\' abbreviation is:', cities['Krakow'])

print('-'*10)
print('Shortcut for Warszawa is: ', cities[voivedoships['Mazowieckie']])

#print every city abbreviation
print('-'*10)
for cities, abbrev in list(cities.items()):
    print(f"{abbrev} has the city {cities}")

#print every city in the state
print('-'*10)
for voivedoships, city in list(voivedoships.items()):
    print(f"{city} is a capitol of {voivedoships} voivedoship ")

print('-'*10)

voivedoship = voivedoships.get('Gdansk')
if not voivedoship:
    print('Sorry, no Gdansk')
