def split_array(arr):
   res = []
   if len(arr) == 1:
        res[0] = arr
   else:
        l = len(arr) // 2
        arr1 = arr[0:l]
        arr2 = arr[l:len(arr)]
        res.append(arr1)
        res.append(arr2)
   return res

#a = [1,2,3,4,5]
#print(a)
#print(split_array(a))

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





#    i = a1.pop()
#    j = a2.pop()
#    while (i != None and j != None):
#        if i == None: 
#            res.append(j)
#            if len(a2) != 0: j = a2.pop()
#            else: j = None
#        elif j == None: 
#            res.append(i)
#            if len(a1) != 0: i = a1.pop()
#            else: i = None
#        elif i <= j:
#          res.append(i)
#          if len(a1) != 0: i = a1.pop()
#          else: i = None
#        else:
#         res.append(j)
#         if len(a2) != 0: j = a2.pop()
#         else: j = None
#    return res

a1 = [1,3,5]
a2 = [2,3,6,7]
print(a1)
print(a2)
r = merge(a1, a2)
print(r)




#def merge_sort(arr):
#    if len(arr) == 1:
#        print('Done!')
#   else:
#        for i in range(0, len(arr), 2):
#            a1 = arr[i]
#            a2 = arr[i+1]
#            print(arr[i], arr[i+1])
#            for j in range(min(len(a1), len(a2))):
#                temp = []
#                temp.append(min(a1[j],a2[j])
#            for j <= max(len(arr)
