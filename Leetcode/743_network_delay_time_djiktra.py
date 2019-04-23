class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        adj_list = collections.defaultdict(dict)
        
        for start,end,weight in times:
            adj_list[start-1][end-1]=weight
            
        to_visit, visited = set(range(N)), set()
        distance = [float('inf')]*N
        
        distance[K-1] = 0
        
        #Loop through all the nodes to be visited
        while to_visit:
            node=None
        #Find the nearest node to visit    
            for item in to_visit:
                if node is None or distance[item] < distance[node]:
                    node = item
        #If cant find the item to visit            
            if distance[node] == float("inf"):
                return -1
        #Found the nearest node to visit    
            to_visit.remove(node)
            visited.add(node)

        #Update the nodes distance    
            for item in adj_list[node]:
                if item not in visited:
                    distance[item] = min(distance[item], 
                                         distance[node]+adj_list[node][item])
        return max(distance)            
            
                