class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = collections.defaultdict(list)
        answer=[]
        for ticket  in tickets:
            adj_list[ticket[0]].append(ticket[1])

        def dfs(node):
            node_list = adj_list[node]
            heapq.heapify(node_list)
            while node_list:
                element = heapq.heappop(node_list)
                dfs(element)
            answer.append(node)    


        dfs("JFK") 

        answer.reverse()
        return answer    
