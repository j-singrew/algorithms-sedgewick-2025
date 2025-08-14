"""
It wants you to modify the Quick-Find union() method to use a weighted strategy:

Track the size of each component.

When merging two components, only change the IDs of the smaller component to the larger one.

After coding it, you should also analyze performance:

Compare how many array updates happen vs normal Quick-Find.

Explain why this improves efficiency (amortized O(log N) per union instead of O(N)).

So the exercise has two parts:

Implement the weighted Quick-Find algorithm in code.

Explain/observe the performance improvement.
"""
class QuickUnionUF:

    def __init__(self,n):
        self.id = list(range(n)) #creates 10 number of id's
        self.parent = n
        self.count = n #number of components
        self.size = n

    
    def find(self,i):
        while i != self.parent[i]: #while i does not equal its idex position value
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
             #set i to the value of  index
        return i 
    
    def connected(self,p,q):
        return self.find(p) == self.find(q) #this will retur true  or false 
    
    def union(self,p,q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return #return true 
        self.id[i] = j
        self.count -=1

    def __str__(self):
        return f"Parent links: {self.id}, Components: {self.count}"
    
    
uf = QuickUnionUF(10)
uf.union(3, 4)
uf.union(4, 9)
print(uf.connected(3, 9))  # True
print(uf)

