   
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Map each course to its prereq list
        answer=[]

        preMap = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visitSet = set() # All courses along the current DFS path
        visited = set()

        
        def dfs(crs):
            # Base cases:
            # 1. If we hit a course already in our path, we found a cycle!
            if crs in visitSet:
                return False

            if crs in visited:
                return True    
       
            # Action:
            visitSet.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): # If any prereq has a cycle, return False
                    return False
                    
            # Cleanup: Remove from path, and clear its prereqs so we never check it again
            visitSet.remove(crs)
            visited.add(crs)
            answer.append(crs)
            
            return True
            
        # Run DFS for every course
        for c in range(numCourses):
            if not dfs(c): 
                return []
            
        return answer
