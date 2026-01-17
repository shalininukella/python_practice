# Time Complexity: O(n × n × 4) In the worst case, every cell in the grid may contain an orange, and for each rotten orange we explore 4 directions (up, down, left, right). So we iterate through all cells (n × n) and perform 4 operations per orange. Hence, the complexity becomes O(n × n × 4), which simplifies to O(n²).

# Space Complexity: O(n × n) In the worst case, all the oranges might be rotten and will be stored in the queue simultaneously. The maximum size of the queue can be equal to the total number of oranges in the grid, i.e., n × n. Therefore, the space complexity is O(n²).

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        q = deque()
        fresh_cnt = 0

        m = len(grid)
        n = len(grid[0])

        # add the rotten oranges to the queue also count the no. of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_cnt += 1

        # intially only the grid has no fresh oranges, so elaped in 0 mins
        if fresh_cnt == 0:
            return 0

        # no cell has the rotten oranges, also handling the case when there's a single empty cell
        if not q:
            return -1

        # coordinates in all the four directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mins = 0

        # bsf in all the four dirs
        while q:
            size = len(q)

            for k in range(size):
                x, y = q.popleft()

                for dx, dy in directions:
                    i = x + dx
                    j = y + dy

                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        q.append((i, j))
                        grid[i][j] = 2
                        fresh_cnt -= 1

            # If queue still has items, increment minutes
            if q:
                mins += 1

        # Return minutes if all rotted, else -1
        if fresh_cnt != 0:
            return -1
        else:
            return mins

# https://leetcode.com/problems/rotting-oranges/submissions/1888004958/
