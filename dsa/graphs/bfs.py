
# Time Complexity: O(V) + O(2E), Where V = Nodes, 2E is for total degrees as we traverse all adjacent nodes.
# == O(V + E)

# Space Complexity: O(3V) ~ O(V), Space for queue data structure visited array and an adjacency list

class Solution:
    def bfsOfGraph(self, V, adj):

        visited = [False] * V
        res = []
        q = deque()

        q.append(0)
        visited[0] = True

        while q:

            node = q.popleft()
            res.append(node)

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True

        return res
