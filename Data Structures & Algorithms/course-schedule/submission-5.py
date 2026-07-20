class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Map each course to its prereq list
        preMap = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visitSet = set() # All courses along the current DFS path
        
        def dfs(crs):
            # Base cases:
            # 1. If we hit a course already in our path, we found a cycle!
            if crs in visitSet:
                return False
                
            # 2. If it has no prereqs (or we already cleared them), it's safe!
            if preMap[crs] == []:
                return True
            
            # Action:
            visitSet.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): # If any prereq has a cycle, return False
                    return False
                    
            # Cleanup: Remove from path, and clear its prereqs so we never check it again
            visitSet.remove(crs)
            preMap[crs] = []
            
            return True
            
        # Run DFS for every course
        for c in range(numCourses):
            if not dfs(c): 
                return False
            
        return True
