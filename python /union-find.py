
class UnionFind:
    def __init__(self,n):
        self.count =n
        self.parent = list(range(n))
        self.size = [1] * n

    
    def find(self,i): #accepts argument p

        while i != self.parent[i]: #while argument p does not equal its parent 
            self.parent[i] = self.parent[self.parent[i]] #assing the value in index [p] to self.parent[p]
            i=self.parent[i]# assign  p to the new value of self 
        return i
    
    def connected(self,p,q): #check if the paths of two number connect 
        return self.find(p)==self.find(q)
    
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
            self.size[rootP] +=self.size[rootQ]
        
        self.count -=1


    

uf = UnionFind(10)

uf.union(4, 3)
uf.union(3, 8)
uf.union(6, 5)
uf.union(9, 4)
uf.union(2, 1)
uf.union(5, 0)
uf.union(7, 2)
uf.union(6, 1)


print("Are 8 and 9 connected?", uf.connected(8, 9))  # ➜ True
print("Are 5 and 4 connected?", uf.connected(5, 4))  # ➜ False