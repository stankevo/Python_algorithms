# demonstrate hashtable usage


# TODO: create a hash table all at once
hash_table = dict({'key1': 1, 'Key2': 2, 'Key3': 'three', 'key4': 4})
print(hash_table)


# TODO: create a hashtable progressively
table2 = {}
table2['Key1'] = 1
table2['Key2'] = 2
table2['Key3'] = 3
table2['Key4'] = 4
print(table2)

# TODO: try to access a nonexistent key
try:
    print(table2['Key6'])
except KeyError as e:
    print("Key doesn't exist")


# TODO: replace an item
table2['Key2'] = 'two'
print(table2)

# TODO: iterate the keys and values in the dictionary
for key, value in table2.items():
    print(f'{key}: {value}')
