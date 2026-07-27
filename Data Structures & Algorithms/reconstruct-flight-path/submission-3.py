class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = collections.defaultdict(list)
        answer = []
        
        # 1. Build Adjacency List
        for src, dst in tickets:
            adj_list[src].append(dst)

        # 2. Sort all lists in REVERSE alphabetical order
        for key in adj_list:
            adj_list[key].sort(reverse=True)

        # 3. Post-Order DFS
        def dfs(node):
            # While the airport still has tickets in its list
            while adj_list[node]:
                # .pop() grabs the last element in O(1) time
                # Because we reverse-sorted, the last element is the alphabetically smallest!
                next_dest = adj_list[node].pop()
                dfs(next_dest)
            
            # Hit a dead end! Add to answer.
            answer.append(node)    

        dfs("JFK") 
        
        # Return the reversed list!
        return answer[::-1]
