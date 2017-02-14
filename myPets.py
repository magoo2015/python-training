myPets = ['Butch', 'Pookie', 'Dat bitch']
print('Enter a pet name')
name = raw_input()
if name not in myPets:
    print('I do not have a bitch named ' + name)
else:
    print(name + ' is my pet.')
