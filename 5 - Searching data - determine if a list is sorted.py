def is_sorted(listItems):
    for i in range(0,len(listItems)-1):
        if listItems[i] > listItems[i+1]:
            return False
    return True

# option 2: using Python expressions
def is_sorted2(listItems):
    return all(listItems[i] <= listItems[i+1] for i in range(len(listItems)-1))

def main():
    l1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
    print(l1)
    print(is_sorted(l1))
    print(is_sorted2(l1))

    l2 = [0,1,2,3,4,5,6,6,5]
    print(l2)
    print(is_sorted(l2))
    print(is_sorted2(l2))

    l3 = [1]
    print(l3)
    print(is_sorted(l3))
    print(is_sorted2(l3))

    l4 = []
    print(l4)
    print(is_sorted(l4))
    print(is_sorted2(l4))

    l5 = [1,1,1,1,1,1,1,1]
    print(l5)
    print(is_sorted(l5))
    print(is_sorted2(l5))


if __name__ == '__main__': main()

