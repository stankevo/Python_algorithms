def quickSort(arr):
    if len(arr) > 1:
        print('Start quick sort.')
        pivot = arr[0]
        print('Pivot: {pivot}')
        loverIndex = 1
        upperIndex = len(arr)-1
        print(f'loverIndex: {loverIndex} - [{arr[loverIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
        while (loverIndex < upperIndex):
            while (arr[loverIndex] < pivot) and (loverIndex < upperIndex):
             loverIndex += 1
             print(f'loverIndex: {loverIndex} - [{arr[loverIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
            while (arr[upperIndex] > pivot) and (loverIndex < upperIndex):
             upperIndex -= 1
             print(f'loverIndex: {loverIndex} - [{arr[loverIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
            temp = arr[loverIndex]
            arr[loverIndex] = arr[upperIndex]
            arr[upperIndex] = temp
            print(f'iteration: {arr}')
        upperIndex -=1
        print(f'upperIndex: {upperIndex} - [{arr[upperIndex]}]')
        temp = arr[upperIndex]
        arr[upperIndex] = pivot
        a[0] = temp
        quickSort(arr[:upperIndex])
        quickSort(arr[upperIndex+1:])
        


a = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(a)
quickSort(a)
print(a)