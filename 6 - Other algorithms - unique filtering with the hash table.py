def removeDuplicates(listItems):
    d = {}
    for key in listItems:
        d[key] = 0
    return list(d.keys())
    
    

l = [1,1,1,2,2,3]
print(l)
print(removeDuplicates(l))


items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]
print(items)
print(removeDuplicates(items))