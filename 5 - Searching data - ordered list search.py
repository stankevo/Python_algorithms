# serach in ordered list via recursion:

def find(item, listItem, start = None, stop = None):
    if start == None: start = 0
    if stop == None: stop = len(listItem)
    if start == stop-1:
        if listItem[start] == item:
            return start
        else:
            return None
    else:
        mid = (start + stop - 1)  // 2
        #print(f'start = {start}, stop = {stop}, mid = {mid} - {listItem[mid]}')
        if listItem[mid] == item:
            #print(f'{mid}')
            return mid
        elif item < listItem[mid]:
            #print(f'find({item}, listItem, {start}, {mid})')
            return find(item, listItem, start, mid)
            #print(f'foo1, {mid}')
        else:
            #print(f'find({item}, listItem, {mid+1}, {stop})')
            return find(item, listItem, mid+1, stop)
            #print(f'foo2, {mid}')

def find1(q):
    return q

        #0   1  2   3   4   5   6   7   8   9
items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
print(items)
print(f'find 65: {find(56, items)}')
print(f'find 1000: {find(1000, items)}')

items = [2]
print(items)
print(f'find 65: {find(56, items)}')
print(f'find 2: {find(2, items)}')





