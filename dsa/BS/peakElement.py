"""edge case explanation"""

# question --- if the mid == 0 then mid-1 should be out of bounds right !!

# then yes: when `mid = 0`, `nums[mid-1]` would be **out of bounds** 🚨.
# That’s why in your *first version* you had to add those extra **boundary checks**:

# ```python
# if nums[0] > nums[1]: return 0
# if nums[n-1] > nums[n-2]: return n-1
# ```

# to handle the ends safely.

# ---

# ### 🔹 But in the **slope-based version** we discussed:

# ```python
# while low < high:
#     mid = (low + high) // 2
#     if nums[mid] > nums[mid+1]:
#         high = mid
#     else:
#         low = mid + 1
# return low
# ```

# 👉 We **never** access `nums[mid-1]`, only `nums[mid+1]`.
# And because the loop condition is `low < high`, we guarantee that `mid < high ≤ n-1`, so `mid+1` is always valid. ✅

# So the boundaries take care of themselves — no risk of out-of-bounds.

# ---

# ### 🔎 Key takeaway:

# * **Explicit-peak-check method** → you must guard against `mid-1` or `mid+1` being out of range.
# * **Slope-based method** → safe by design, because it only looks one step right, and the loop condition ensures that index exists.

# ---
# question - if the mid == n-1 (last element), then the mid+1 should raise outofbounds right!!
# ### The code we’re talking about:

# ```python
# while low < high:
#     mid = (low + high) // 2
#     if nums[mid] > nums[mid+1]:
#         high = mid
#     else:
#         low = mid + 1
# return low
# ```

# ---

# ### 🔹 Could `mid` ever be the **last index**?

# * The loop condition is `low < high`.
# * That means `mid = (low+high)//2` is **always strictly less than `high`**.
# * Since `high ≤ n-1`, we guarantee `mid ≤ n-2`.
# * Therefore, `mid+1 ≤ n-1` → always safe ✅.

# ---

# ### 🔎 Example: `low=high=n-1`

# This would mean we’re done — the loop ends (`low < high` fails).
# So we never compute `mid = n-1` inside the loop.

# ---

# ✅ **Conclusion**: `mid+1` will never go out of bounds in this algorithm.
# That’s the beauty of the slope-based binary search — the `while low < high` condition makes sure the “look right” check is always valid.

# ---

# Would you like me to **prove this with math** (show that `mid <= n-2` always inside the loop), or would you prefer a **step-by-step dry run** with `n=5` to see how `mid` evolves?

# brute force
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         n = len(nums)

#         if n == 1:
#             return 0

#         if nums[0] > nums[1] :
#             return 0
#         if nums[n-1] > nums[n-2]:
#             return n-1

#         low = 0
#         high = n-1
#         while low < high:
#             mid = low + (high - low) // 2
#             if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
#                 return mid
#             elif nums[mid+1] > nums[mid]:
#                 #go right, cuz it's increasing on the right, peak will be on the right side for sure
#                 low = mid+1
#             else:
#                 #a[mid-1]>a[mid]:
#                 #go right, cuz it's increasing on the right, peak will be on the right side for sure
#                 high = mid-1
#         #returning low cuz the loop will be exited only when the low == high
#         return low


# or to avoid checking the boundaries or checking the mid>mid+1 or mid>mid-1 explicitly
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid + 1]:
                # offcourse mid or another element on the left will be the peak
                high = mid
            else:
                # when the nums[mid] < nums[mid+1] :
                # ofcourse mid is not the peak, any elem after mid i.e on the right is the peak
                low = mid + 1
        return low


# question

# https://leetcode.com/problems/find-peak-element/
