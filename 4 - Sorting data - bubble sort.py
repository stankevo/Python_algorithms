def bubbleSort(arr):
    l = len(arr)
    sorted = False
    while (sorted != True):
        sorted = True
        for i in range(l-1):
            if arr[i] > arr[i+1]:
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t
                sorted = False
    return arr

a = [1,3,6,3,2]
print(a)
bubbleSort(a)
print(a)