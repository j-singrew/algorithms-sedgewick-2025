



#Develop classes QuickUnionUF and QuickFindUF that implement quick-union
#and quick-find, respectively.


class QuickUnionUF:

    def __init__(self,n):
        self.id = list(range(n)) #creates 10 number of id's
        self.count = n #number of components

    
    def root(self,i):
        while i != self.id[i]: #while i does not equal its idex position value
            i = self.id[i] #set i to the value of  index
        return i 
    
    def connected(self,p,q):
        return self.root(p) == self.root(q) #this will retur true  or false 
    
    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)
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