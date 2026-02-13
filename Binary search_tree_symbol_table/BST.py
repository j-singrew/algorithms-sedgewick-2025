def recusive_binary_search(arr,low,high,x):
    if high >= low:
        mid =  low + (high- low)//2

        if arr[mid] == x:
            return mid
    
        elif arr[mid] > x:
            return recusive_binary_search(arr,low,mid-1,x)
        else:
            return recusive_binary_search(arr,low+1,high,x)
    else:
        return -1
    


arr = [2, 3, 4, 10, 40]
x = 10

result = recusive_binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")
