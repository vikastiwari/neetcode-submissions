class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Array where each node is its own parent initially (nodes are 1 to n)
        parent = [i for i in range(len(edges) + 1)]
        
        # Array to track the size of the set (for optimization)
        rank = [1] * (len(edges) + 1)

        # "Find" function: Follows the chain until it finds the top boss
        def find(n):
            p = parent[n]
            while p != parent[p]:
                # Path compression (optional but makes it super fast)
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        # "Union" function: Merges two sets
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            # If they already have the same boss, we found the redundant edge!
            if p1 == p2:
                return False
                
            # Otherwise, merge the smaller set into the larger set
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True

        # Loop through edges. The first one that returns False is the answer!
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
