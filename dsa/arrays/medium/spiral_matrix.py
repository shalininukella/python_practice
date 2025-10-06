class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = cols - 1
        top = 0
        bottom = rows - 1

        res = []

        while left <= right and top <= bottom:

            # top row - left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # left most col - top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # bottom row - right to left
            # also include the edge case where there's only one row, so that we don't traverse it in the backward direction
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # left most col - bottom to top
            # also include the edge case where there's only one col, so that we don't traverse it in the backward direction
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


# https://leetcode.com/problems/spiral-matrix/
