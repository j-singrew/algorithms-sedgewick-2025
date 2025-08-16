class weighted_quick_find:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self,i):

        if i == self.parent[i]:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self,p,q):

        rootQ = self.find(q)
        rootP = self.find(p)

        if rootQ == rootP:
            return 
        
        #combining root's 
        if self.size[rootP] < self.size[rootQ]:
               
               self.parent[rootP] = rootQ
               self.size[rootQ] += self.size[rootP]
            
        else:

            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
