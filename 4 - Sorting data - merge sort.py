#def split_array(arr):
#    res = []
#    if len(arr) == 1:
#        res.append = arr
#        print(res)
#        return (res)
#    else:
#        l = len(arr) // 2
#        arr1 = arr[0:l]
#        arr2 = arr[l:len(arr)]
#        split_array(arr1)
#        split_array(arr2)


#        res.append(arr1)
#        res.append(arr2)
#        print(res)
#        return res


def merge_sort(arr):
    if len(arr) == 1:
        print('Done!')
    else:
        for i in range(0, len(arr), 2):
            a1 = arr[i]
            a2 = arr[i+1]
            print(arr[i], arr[i+1])
            for j in range(min(len(a1), len(a2))):
                temp = []
                temp.append(min(a1[j],a2[j])
            for j <= max(len(arr)
