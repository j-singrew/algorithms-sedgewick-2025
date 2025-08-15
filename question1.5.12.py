"""
1.5.12 Quick-union with path compression. Modify quick-union (page 224) to include
path compression, by adding a loop to union() that links every site on the paths from
p and q to the roots of their trees to the root of the new tree. Give a sequence of input
pairs that causes this method to produce a path of length 4. Note : The amortized cost
per operation for this algorithm is known to be logarithmic.
"""
class QuickUnionUF:

    def __init__(self,n):
        self.id = list(range(n)) 
        self.count = n 

    
    def root(self,i):
        while i != self.id[i]:
            i = self.id[i] 
        return i 
    
    def connected(self,p,q):
        return self.root(p) == self.root(q)
    
    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return 
        self.id[i] = j
        self.count -=1

    def __str__(self):
        return f"Parent links: {self.id}, Components: {self.count}"
    
    
uf = QuickUnionUF(10)
uf.union(3, 4)
uf.union(4, 9)
print(uf.connected(3, 9))
print(uf)
