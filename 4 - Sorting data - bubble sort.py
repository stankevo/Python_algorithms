def bubbleSort(arr):
    l = len(arr)
    sorted = False
    print('\nstart iterations:')
    while (sorted != True):
        sorted = True
        for i in range(l-1):
            if arr[i] > arr[i+1]:
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t
                sorted = False
        print(arr)
    return arr

a = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(f'initial array:\n{a}')
bubbleSort(a)
print(f'\nsorted array:\n{a}')