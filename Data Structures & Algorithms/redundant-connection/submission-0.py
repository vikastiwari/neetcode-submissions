class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(len(edges)-1,-1,-1):
            newedge=edges[:i] + edges[i+1:]
            if self.validTree(len(edges),newedge):
                return edges[i] 


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge case: A tree must have exactly n - 1 edges. 
        # If it doesn't, it's mathematically impossible to be a valid tree!
        if len(edges) != n - 1:
            return False

        # 1. Build the Adjacency List (undirected, so add both directions)
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1-1].append(n2-1)
            adj[n2-1].append(n1-1)

        visit = set()

        def dfs(node, parent):
            # If we hit a node we already visited, we found a cycle!
            if node in visit:
                return False

            visit.add(node)
            
            # Go through all neighbors
            for neighbor in adj[node]:
                # Don't go backwards to the parent we just came from!
                if neighbor == parent:
                    continue
                
                # If any neighbor finds a cycle, the whole thing fails
                if not dfs(neighbor, node):
                    return False
                    
            return True

        # 2. Run DFS starting from node 0 (with no parent, so we pass -1)
        # If it returns False, there is a cycle.
        if not dfs(0, -1):
            return False
            
        # 3. Final Check: Did we connect to every single node?
        # If len(visit) == n, it means it's fully connected (no islands!)
        return len(visit) == n
    
        