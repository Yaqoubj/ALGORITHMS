def BinarySearch(arr,x):
    
    low = 0
    high = len(arr)-1 
    while low <= high:    
    # In other languges could cause Intger overflow
        mid = (low+high)//2

        if arr[mid] == x:
            return mid
                
        elif  arr[mid] < x:
            low = mid + 1
        
        else:
            high = mid - 1
    return -1


arr = [1,2,3,4,5,99,115,250]
a = BinarySearch(arr,115)
print(a)