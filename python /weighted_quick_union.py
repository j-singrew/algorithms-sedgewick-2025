"""
Weighted quick-union with path compression. Modify weighted quick-union
(Algorithm 1.5) to implement path compression, as described in Exercise 1.5.12.
Give a sequence of input pairs that causes this method to produce a tree of height 4.
Note : The amortized cost per operation for this algorithm is known to be bounded by a
function known as the inverse Ackermann function and is less than 5 for any conceivable
practical value of N.

"""


class weighted_qick_union:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n

    
    def find(self,p):
        if p == self.parent[p]:
            return
        self.parent[p] = self.find(self.parent[p])
        return self.parent
        
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return 
        
        if self.size[rootP] < self.size[rootQ]:
               
               self.parent[rootP] = rootQ
               self.size[rootQ] += self.size[rootP]
            
        else:

            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]


    