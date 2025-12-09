def Insertion(arr):
    n= len(arr)

    for i in range(1,n):
        k= arr[i]
        j = i-1

        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        #When loop doesn't run: j is still i - 1, so j + 1 = i
        # in short it will nothing if the loop doesnt run    
        arr[j+1] = k

        


arr = [3,2,5,1,7,0]
Insertion(arr)
print(arr)