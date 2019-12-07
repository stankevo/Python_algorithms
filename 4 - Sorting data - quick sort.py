def quickSort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        loverIndex = 1
        upperIndex = len(arr)-1
        while (loverIndex < upperIndex):
            while arr[loverIndex] < pivot:
                loverIndex += 1
            while arr[upperIndex] > pivot:
                loverIndex -= 1
            temp = arr[loverIndex]
            arr[loverIndex] = arr[upperIndex]
            arr[upperIndex] = temp