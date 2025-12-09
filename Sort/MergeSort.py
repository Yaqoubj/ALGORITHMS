def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) //2
    a1 = merge_sort(arr[:mid])
    a2 = merge_sort(arr[mid:])
    return merge(a1,a2)

def merge(a1,a2):
    i,j =0,0
    c = []

    while i < len(a1) and j <len(a2):
        if a1[i] < a2[j]:
            c.append(a1[i])
            i +=1
        else:
            c.append(a2[j])
            j +=1
    if i == len(a1):
        c.extend(a2[j:])
    elif j == len(a2):
        c.extend(a1[i:])
    return c

arr = [3,2,6,1,9,4]
arr = merge_sort(arr)
print(arr)