# Time Complexity: O(V) + O(2E), Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes.
# == O(V + E)
# Space Complexity: O(V)  (visited array + recursion stack)

class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        res = []

        def dfs(node):
            visited[node] = True
            res.append(node)

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        dfs(0)
        return res
