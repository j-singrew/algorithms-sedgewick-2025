#union-find
"""
1.5.17 Random connections. Develop a UF client ErdosRenyi that takes an integer
value N from the command line, generates random pairs of integers between 0 and N-1,
calling connected() to determine if they are connected and then union() if not (as in
our development client), looping until all sites are connected, and printing the number
of connections generated. Package your program as a static method count() that takes
N as argument and returns the number of connections and a main() that takes N from
the command line, calls count(), and prints the returned value.
"""
import random

class RandomConnections:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n














def random_generate(N):
    uf = RandomConnections(N)
    connestions = 0
    while len({uf.find(i) for in range(N)}) >1:
        




         

