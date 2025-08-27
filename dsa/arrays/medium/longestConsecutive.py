class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLen = 0

        for num in seen:  # ✅ avoids duplicates
            if num - 1 not in seen:  # start of a new sequence
                curr = num
                cnt = 1

                while curr + 1 in seen:
                    curr += 1
                    cnt += 1

                maxLen = max(maxLen, cnt)

        return maxLen
# https://leetcode.com/problems/longest-consecutive-sequence/