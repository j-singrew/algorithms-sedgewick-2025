"""
🧱 10 Fundamental Data Structures & Algorithms to Implement

🔹 1. Insertion sort
Teaches: shifting, in-place sorting
Focus: how elements move
Youve already done this — good

🔹 2. Selection sort
Teaches: scanning + minimum tracking
Focus: separating sorted vs unsorted regions

🔹 3. Merge sort
Teaches: recursion + divide and conquer
Focus: splitting and merging
First “serious” algorithm

🔹 4. Binary search
Teaches: logarithmic thinking
Focus: cutting problem size in half
Requires sorted input

🔹 5. Stack
Implement with array or list
Teaches: LIFO (Last In First Out)
Add: push, pop, peek

🔹 6. Queue
Teaches: FIFO (First In First Out)
Add: enqueue, dequeue
Bonus: circular queue

🔹 7. Linked list
Implement:
singly linked list
Teaches: pointers/references
Add:
insert
delete
traversal

🔹 8. Hash table
Teaches: key → index mapping
Implement:
basic hashing
collision handling (chaining)

🔹 9. Binary search tree
Teaches: hierarchical structures
Implement:
insert
search
inorder traversal

🔹 10. Depth-first search (DFS)
Teaches: recursion + graphs
Use:
adjacency list
Foundation for advanced graph problems



"""

def InsertionSort(arr):

    for i in range(1,len(arr)):

        key = arr[i]
        j =i -1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j] 
            j -=1

        arr[j+1] = key





def selectionSort(arr):
    for i in range(0,len(arr)):

        key = arr[i]
        smallestIndex = i
        for x in range(i+1,len(arr)):
                if arr[x]  < arr[smallestIndex]:
                    smallestIndex = x

    arr[i] ,arr[smallestIndex] = arr[smallestIndex],arr[i]

    return arr
    


def Merge(arr,right,left,mid='none'):
     n = len(arr)
     if ((n) % 2) != 0:
          mid = n % 2
          
          
           
          
          
          
     

     

     
     
     
    
     
         