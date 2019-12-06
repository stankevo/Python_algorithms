#def split_array(arr):
#    res = []
#    if len(arr) == 1:
#        res.append = arr
#        print(res)
#        return (res)
#    else:
#        l = len(arr) // 2
#        arr1 = arr[0:l]
#        split_array(arr1)
#        split_array(arr2)
#
#
#
 #       res.append(arr1)
  #      res.append(arr2)
   #     print(res)
    #    return res


#a = [1]
#split_array(a)


def mergeSort(arr):
    if len(arr) == 1:
        print('Done!')
    else:
        a1 = arr[0]
        a2 = arr[1]
        i = 0
        j = 0
        temp = []
        while i < len(a1):
            while j < len(a2):
                if i <= j:
                    temp.append(a1[i])
                    i += 1
                else:
                    temp.append(a2[j])
                    j += 1
        print(temp)

arr = [[2,4], [1,3,5]]
def merge(a1, a2):
    i = a1.pop()
    j = a2.pop()
    temp = []
    while (len(a1) != 0) or (len(a2) != 0):
        if i <= j:
            temp.append(i)
            i = a1.pop()
        else:
            temp.append(j)
            j = a2.pop()
    e1 = a1.pop()
    e2 = a2.pop()
    if e1 != None:
        temp.append(e1)
    if e2 != None:
        temp.append(e2)
    print(temp)


merge([2,4], [1,3,5])
    



        


