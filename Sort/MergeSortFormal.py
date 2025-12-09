def merge(arr,left,mid,right):
    
    n1 = mid - left +1
    n2 = right - mid

    l = [0]*n1
    r = [0]*n2

    for i in range(n1):
        l[i] = arr[left+i]
    for j in range(n2):
        r[j] = arr[mid+j+1]
    
    i,j,k = 0,0,left

    while i < n1 and j < n2:
        if l[i] < r[j]:
            arr[k] = l[i]
            i +=1
            k +=1
        else:
            arr[k] = r[j]
            j +=1
            k +=1
    
    while i < n1:
        arr[k] = l[i]
        i +=1
        k +=1
    while j < n2:
        arr[k] = r[j]
        j +=1
        k +=1


def mergeSort(arr,left,right):
    if left < right :

        mid = (left+right)//2

        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)






arr =[4,2,1,9,4,7,1,3,6,9,63,1]

mergeSort(arr,0,len(arr)-1)

print(arr)