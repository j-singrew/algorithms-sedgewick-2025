"""

2.1.25 Insertion sort without exchanges. Develop an implementation of insertion sort
that moves larger elements to the right one position with one array access per entry,
rather than using exch().

"""

def Insertion_sort(arr):
    
    n = len(arr)

    for i in range(0,n):

        # Value to insert 
        key = arr[i]

        # left point 
        j = i -1

        #Shift element to the right
        while j>=0 and arr[j] > key:
            arr[j + 1] = arr[j] 
            j -=  1

        arr[j + 1] = key   

