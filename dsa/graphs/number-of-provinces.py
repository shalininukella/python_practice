# using BFS

# Time = O(V²) - (adjacency matrix scan) - For each visited node, we scan the entire row in the adjacency matrix
# Space = O(V) - (visited + queue)       

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(V, node):
            q = collections.deque()
            q.append(node)

            visited[node] = True

            while q:
                curr = q.popleft()
                
                for i in range(V):
                    if isConnected[curr][i] == 1 and not visited[i]:
                        q.append(i)
                        visited[i] = True

        V = len(isConnected)          
        cnt = 0
        visited = [False] * V

        for i in range(V):
            if not visited[i]:
                cnt += 1
                bfs(V, i)

        return cnt


# using DFS

# Time = O(V²) - (adjacency matrix scan) - For each visited node, we scan the entire row in the adjacency matrix
# Space = O(V) - (visited + queue)  

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(V, node):
            visited[node] = True

            for i in range(V):
                if isConnected[node][i] == 1 and not visited[i]:
                    dfs(V, i)

        V = len(isConnected)
        visited = [False] * V
        cnt = 0

        for i in range(V):
            if not visited[i]:
                cnt += 1
                dfs(V, i)

        return cnt


# https://leetcode.com/problems/number-of-provinces/submissions/1887755507/