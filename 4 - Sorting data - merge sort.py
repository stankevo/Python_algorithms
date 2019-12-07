def split_array(arr):
   res = []
   if len(arr) == 1:
        res[0] = arr
   else:
        l = len(arr) // 2
        arr1 = arr[:l]
        arr2 = arr[l:]
        res.append(arr1)
        res.append(arr2)
   return res

def merge(a1, a2):
    res = []
    i = 0
    j = 0
    while i < len(a1) or j < len(a2):
        if i >= len(a1):
            res.append(a2[j])
            j += 1
        elif j >= len(a2):
            res.append(a1[i])
            i += 1
        elif a1[i] <= a2[j]:
            res.append(a1[i])
            i += 1
        else:
            res.append(a2[j])
            j += 1
    return res

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        q = [2]
        q = split_array(arr)
        return merge(mergeSort(q[0]), mergeSort(q[1]))

def main():
    w = [1,3,5,2,3,6,0]
    print(f'Unsorted array: {w}')
    w1 = mergeSort(w)
    print(f'Sorted array: {w1}')

    w = [100]
    print(f'Unsorted array: {w}')
    w1 = mergeSort(w)
    print(f'Sorted array: {w1}')

    w = [2,4,3,6,5,1]
    print(f'Unsorted array: {w}')
    w1 = mergeSort(w)
    print(f'Sorted array: {w1}')

    w = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print(f'Unsorted array: {w}')
    w1 = mergeSort(w)
    print(f'Sorted array: {w1}')

if __name__ == '__main__': main()