def quickSort(arr):
    if len(arr) > 1:
        print('Start quick sort.')
        if len(arr) == 1:
            print(f'iteration: {arr}')
            return arr
        else:
            pivot = arr[0]
            print(f'Pivot: {pivot}')
            loverIndex = 1
            upperIndex = len(arr)-1
            print(f'loverIndex: {loverIndex} - [{arr[loverIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
            while (loverIndex < upperIndex): # move indexes and switch items untill indexes mit
                while (arr[loverIndex] < pivot) and (loverIndex < upperIndex):
                    loverIndex += 1
                    print(f'loverIndex: {loverIndex} - [{arr[loverIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
                while (arr[upperIndex] > pivot) and (loverIndex < upperIndex):
                    upperIndex -= 1
                    print(f'loverIndex: {loverIndex} - [{arr[loverIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
                temp = arr[loverIndex]
                arr[loverIndex] = arr[upperIndex]
                arr[upperIndex] = temp
            
            # put pivot into the right place
            print(f'before putting pivot: {arr}')
            if arr[upperIndex] > pivot:
                upperIndex -=1
            print(f'upperIndex: {upperIndex} - [{arr[upperIndex]}]')
            if upperIndex != 0:
                temp = arr[upperIndex]
                arr[upperIndex] = pivot
                arr[0] = temp
                print(f'iteration: {arr}')
                print(f'split array: {arr[:upperIndex]} - {pivot} - {arr[upperIndex+1:]}')
                quickSort(arr[:upperIndex])
                quickSort(arr[upperIndex+1:])
            else:
                print(f'split array: {pivot} - {arr[upperIndex+1:]}')
                quickSort(arr[upperIndex+1:])

        


a = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(a)
print(quickSort(a))