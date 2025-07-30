public class UnionFind {
    private int[] parent;  // parent[i] points to the parent of i
    private int[] size;    // size[i] = number of nodes in subtree rooted at i
    private int count;     // number of components

    // Constructor: initialize N elements
    public UnionFind(int N) {
        count = N;
        parent = new int[N];
        size = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;   // each node is its own parent
            size[i] = 1;     // each component is size 1
        }
    }

    // Return number of components
    public int count() {
        return count
    }

    // Find the root of element p with path compression
    public int find(int p) {
        while (p != parent[p]) {
            parent[p] = parent[parent[p]]; // path compression (one-pass)
            p = parent[p];
        }
        return p;
    }

    // Are p and q connected?
    public boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    // Connect p and q by size
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);

        if (rootP == rootQ) return;

        // Make smaller tree point to larger one
        if (size[rootP] < size[rootQ]) {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        } else {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        }

        count--;
    }
}