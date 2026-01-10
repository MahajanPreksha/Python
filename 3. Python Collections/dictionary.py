#Creating a dictionary
phones = {'John': 1111, 'Ria': 2222, 'Joy': 3333}

#Printing a dictionary
print(phones)  #Output: {'John': 1111, 'Ria': 2222, 'Joy': 3333}

#Checking the type of a dictionary
print(type(phones))  #Output: <class 'dict'>

#Length of a dictionary
print(len(phones))  #Output: 3

#Accessing items of a dictionary
print(phones['Ria'])  #Output: 2222
print(phones.get('Joy'))  #Output: 3333
print(phones.keys())  #Output: dict_keys(['John', 'Ria', 'Joy'])

#Updating values in a dictionary
phones['John'] = 4444
print(phones)  #Output: {'John': 4444, 'Ria': 2222, 'Joy': 3333}

#Adding new items to a dictionary
phones['Kia'] = 5555
print(phones)  #Output: {'John': 4444, 'Ria': 2222, 'Joy': 3333, 'Kia': 5555}

more_phones = {'Sia': 6666}
phones.update(more_phones)
print(phones)  #Output: {'John': 4444, 'Ria': 2222, 'Joy': 3333, 'Kia': 5555, 'Sia': 6666}

#Removing items from a dictionary
phones.pop('Ria')
print(phones)  #Output: {'John': 4444, 'Joy': 3333, 'Kia': 5555, 'Sia': 6666}

phones.popitem()
print(phones)  #Output: {'John': 4444, 'Joy': 3333, 'Kia': 5555}

phones.clear()
print(phones)  #Output: {}

#Printing values of a dictionary
phones = {'John': 1111, 'Ria': 2222, 'Joy': 3333}

for x in phones.values():
    print(x)
#OR
for x in phones:
    print(phones[x])

'''Output:
1111
2222
3333
'''

#Printing both keys and values i.e. elements of a dictionary
for x, y in phones.items():
    print(x, y)

'''Output:
John 1111
Ria 2222
Joy 3333
'''

#Nested dictionaries
areas = {
    "Area1": {
        "x": 0,
        "y": 1,
        "z": 2
    },
    "Area2": {
        "a": 3,
        "b": 4,
        "c": 5
    }
}

print(areas['Area1']['y'])  #Output: 1
print(areas['Area2']['b'])  #Output: 4