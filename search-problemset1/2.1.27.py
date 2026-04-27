"""
2.1.27 Shellsort is subquadratic. Use SortCompare to compare shellsort with insertion
sort and selection sort on your computer. Use array sizes that are increasing powers of
2, starting at 128.

"""
"""

shellshort 

"""


def shellShort(arr):
    #Array size
    n = len(arr)
    #gap calculartion formula 
    gap = n // 2

    while  gap > 0:
        for i in range(gap,len(arr)):

            #current index value
            temp = arr[i]
            #current index 
            j = i
            # j >=  gap Check that j (index) is larger  or exactly equal to gap ,becuase if value is smaller than gap is not enforced 
            # arr[j-gap] > temp checks that the prevouse gap value is bigger than current  
            while j >=  gap and arr[j -  gap] > temp:
                #set current value equal to bigger prevouse value 
                arr[j] = arr[j - gap]
                
                #set index value to prevouse value 
                j = j - gap
            #change current index value to temp value 
            arr[j] = temp
        #recalculate gap
        gap //= 2

def insertionSort(arr):


    for i in range(1,len(arr)):

        #value store for array value
        temp = arr[i]
        #prevouse index value
        j = i-1

        #while j >= 0 and arr[j-1] is larger than temporary varuable 
        while j >= 0 and  arr[j] > temp:
            #Set j equal to  i
            arr[j+1] = arr[j] 
            #set j to prevouse variable for loop 
            j = j-1

        #when while has completed set the temp to a new value 
        arr[j+1] = temp



def selectionSort(arr):

    n = len(arr)
    for i in range(0,n):
        temp = arr[i]
        smallest_index = i 
        for x in range(i+1,n):
            print(i,n)
    

            if arr[x] <  arr[smallest_index]:
                smallest_index= x
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr



            





















    
