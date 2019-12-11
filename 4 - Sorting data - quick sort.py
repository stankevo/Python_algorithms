def quickSort(arr, start = 0, end = None):
    
    # set lowerIndex and upperIndex
    lowerIndex = start
    if end != None:
        upperIndex = end
    else: upperIndex = len(arr)-1

    if len(arr[lowerIndex:upperIndex+1]) > 1:
        #print(f'Start quick sort on {arr[lowerIndex:upperIndex+1]}')
        
        # set pivot
        pivot = arr[start]
        lowerIndex += 1

        #start sorting
        #print(f'pivot: {pivot}, lowerIndex: {lowerIndex} - [{arr[lowerIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
        # move indexes and switch items untill indexes mit
        while (lowerIndex < upperIndex):
            while (arr[lowerIndex] < pivot) and (lowerIndex < upperIndex):
                lowerIndex += 1
                #print(f'lowerIndex: {lowerIndex} - [{arr[lowerIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
            while (arr[upperIndex] > pivot) and (lowerIndex < upperIndex): 
                upperIndex -= 1
                #print(f'lowerIndex: {lowerIndex} - [{arr[lowerIndex]}]; upperIndex: {upperIndex} - [{arr[upperIndex]}]')
            if arr[lowerIndex] > arr[upperIndex]:
                temp = arr[lowerIndex]
                arr[lowerIndex] = arr[upperIndex]
                arr[upperIndex] = temp
                #print(f' items {arr[lowerIndex]} and {arr[upperIndex]} switched.')
                #print(arr)

            
        # put pivot into the right place
        #print(f'before putting pivot: {arr}')
        if arr[upperIndex] > pivot:
            upperIndex -=1
            #print(f'upperIndex: {upperIndex} - [{arr[upperIndex]}]')
        temp = arr[upperIndex]
        pivotIndex = arr.index(pivot)
        arr[upperIndex] = pivot
        arr[pivotIndex] = temp
        #print(f' after inserting pivot: \n{arr}')
        #print(f'split array: {arr[:upperIndex]} - {pivot} - {arr[upperIndex+1:]}')
        quickSort(arr, upperIndex+1, end)
        quickSort(arr, start, upperIndex)
            

a = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(a)
quickSort(a)
print(f'sorted array: \n{a}')

a = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
print(f'\n{a}')
quickSort(a)
print(f'sorted array: \n{a}')

a = [1]
print(f'\n{a}')
quickSort(a)
print(f'sorted array: \n{a}')