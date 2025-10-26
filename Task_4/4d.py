dictionary={'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dictionary)
#Access Values: Access values using keys.
print(dictionary['name'])
print(dictionary['age'])

#Modify Dictionary: Update values, add new key-value pairs, and remove existing pairs.
dictionary['name']= "James"
print(dictionary)
dictionary.pop('city')
print(dictionary)
#Iterate Over Dictionary: Use loops to iterate over keys or values.
for k in dictionary:
    print("KEY:",k)

print(dictionary.items())

output:
{'name': 'Alice', 'age': 30, 'city': 'New York'}
Alice
30
{'name': 'James', 'age': 30, 'city': 'New York'}
{'name': 'James', 'age': 30}
KEY: name
KEY: age
dict_items([('name', 'James'), ('age', 30)])
