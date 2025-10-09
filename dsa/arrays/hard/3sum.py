##1 works but TLE

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)

        # for i in range (n-2):
        #     ele = nums[i]
        #     target_2sum = 0 - ele

        #     seen = defaultdict(int) #unique for each 2 sum

        #     for j in range(i+1, n):
                
        #         curr = nums[j]
        #         rem = target_2sum - curr

        #         unique_triplet = []

        #         if rem in seen:
        #             unique_triplet.append(rem)
        #             unique_triplet.append(curr)
        #             unique_triplet.append(ele)

        #             unique_triplet.sort() #to put the unique triplets

        #             if unique_triplet not in res:
        #                 res.append(unique_triplet)

        #         seen[nums[j]] = j #or seen[curr] = j
        # return res



##2 TLE and doesn't work for [0,0,0,0]
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()  # Sorting the input array first
#         n = len(nums)

#         for i in range(n - 2):
#             # Skip duplicates for the first number in the triplet
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             target_2sum = -nums[i]
#             seen = set()  # Set to track the second and third elements in the triplet

#             for j in range(i + 1, n):
#                 rem = target_2sum - nums[j]

#                 # Check if the complement is in the set (we have found a valid triplet)
#                 if rem in seen:
#                     res.append([nums[i], nums[j], rem])

#                     # Skip duplicates for the second number in the triplet
#                     while j + 1 < n and nums[j] == nums[j + 1]:
#                         j += 1

#                 # Add the current element to the set
#                 seen.add(nums[j])

#         return res


## 3 efficient - no tle

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort the array to handle duplicates easily and use two-pointer approach
        n = len(nums)

        for i in range(n - 2):  # We need at least 3 numbers to form a triplet
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target_2sum = -nums[i]  # We want two numbers that sum up to -nums[i]
            left, right = i + 1, n - 1  # Two-pointer approach for the rest of the array

            while left < right:
                two_sum = nums[left] + nums[right]

                if two_sum == target_2sum:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second number (nums[left])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the third number (nums[right])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1

                elif two_sum < target_2sum:  # We need a larger sum, move the left pointer to the right
                    left += 1
                else:  # We need a smaller sum, move the right pointer to the left
                    right -= 1

        return res
    
# https://leetcode.com/problems/3sum/description/