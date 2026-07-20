class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i : [] for i in range(n) }
        answer=0
        for node1,node2 in edges:
            preMap[node1].append(node2)
            preMap[node2].append(node1)
        visited=set()    

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)    

            for cell in preMap[node]:
                if cell not in visited:
                    dfs(cell)

        for i in range(n):
            if i not in visited:
                answer+=1
                dfs(i)

        return answer        


        