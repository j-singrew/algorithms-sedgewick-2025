"""
2.1.24 Insertion sort with sentinel. Develop an implementation of insertion sort that
eliminates the j>0 test in the inner loop by first putting the smallest item into position.

inveriant - After i-th iteration ,the subarray arr[1,i] is sorted,all elemnts are  >= arrr[0]
"""


#iterate through array find the smallest values 
#set that value to index[0]

#iterate and sort th rest of the values  into sorted order 
"""
    Preprocessing list/arry using sentinal to identify true smallest element and move it into index 0

"""
def sentinal(arr):

    min_index = 0 
    for  i in range(1,len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i


    arr[0], arr[min_index] = arr[min_index], arr[0]
    print(arr)

    return arr



def insertionSort(arr):
    """
    Preprocessing - arr 
    
    """
    n_arr = sentinal(arr)
    """
    LOOP through array 

    """
    for i in range(1,len(n_arr)):
        current_key = n_arr[i]
        print(current_key)
        j =i - 1

        #Compare current key to prevouse key
        while current_key < n_arr[j]:
            #setting j to the value of i
            n_arr[j + 1] = n_arr[j]
            #reseting j 
            j -= 1
            print("i",i)
            print("j",j)
            print(n_arr)
        #Iterating through list setting new keys
        n_arr[j + 1 ] = current_key



if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)








        

    




