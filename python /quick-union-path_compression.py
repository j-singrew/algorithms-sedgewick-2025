#the one with the tree 
"""
Weighted quick-union with path compression. Modify weighted quick-union
(Algorithm 1.5) to implement path compression, as described in Exercise 1.5.12.
Give a sequence of input pairs that causes this method to produce a tree of height 4.
Note : The amortized cost per operation for this algorithm is known to be bounded by a
function known as the inverse Ackermann function and is less than 5 for any conceivable
practical value of N.
"""
def __init__(self,n):
    self.parent = list(range(n))
    self.size = 1


def root(self,p):
    while p != self.parent[p]:
        p = self.parent[p]
    return p 


            






