def countUniqueValues(items):
    d = {}
    for key in items:
        if key in d.keys():
            d[key] +=1
        else: d[key] = 1
    return d

def main():
    l = [1,1,1,2,2,3]
    print(l)
    print(countUniqueValues(l))

    items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]
    print(items)
    print(countUniqueValues(items))

if __name__ == '__main__': main()