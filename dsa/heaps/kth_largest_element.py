class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)

            # pops the smallest elements and then reheapify the heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# https://leetcode.com/problems/kth-largest-element-in-an-array/
