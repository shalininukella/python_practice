"""
3. Finding Prefix Product and Suffix Product
Similar to finding Prefix Sum Array, here we would intend to find the Prefix Product Array and Suffix Product Array for our original array, i.e. pre[i] = pre[i - 1] * a[i - 1] (yes, we multiply with a[i - 1] and not with a[i] on purpose) and similarly suff[i] = suff[i + 1] * a[i + 1].
Now, at any index i our final answer ans[i] would be given by ans[i] = pre[i] * suff[i]. Why? Because the pre[i] * suff[i] contains product of every element before i and every element after i but not the element at index i (and that is the reson why we excluded a[i] in our prefix and suffix product).

The Time Complexity would be O(n), but we are now using Auxilary Space of O(n) (excluding the final answer array).
"""

# #tc = 0(n)
# #sc = 0(n) - pre and suf arrays

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         pre = [None]*n
#         suf = [None]*n
#         pre[0] = 1
#         suf[n-1] = 1
#         ans = [None] * n

#         #contains the prefix product except the current element
#         for i in range(1, n):
#             pre[i] = pre[i-1] * nums[i-1]
        
#         #contains the suffix product except the current element
#         for i in range(n-2, -1, -1):
#             suf[i] = suf[i+1] * nums[i+1]

#         #Because the pre[i] * suf[i] contains product of every element before i and every element after i but not the element at index i (and that is the reson why we excluded a[i] in our prefix and suffix product).
#         for i in range(n):
#             ans[i] = pre[i] * suf[i]
        
#         return ans

"""
4. Directly store the product of prefix and suffix into the final answer array
The logic is, we don't actually need seperate array to store prefix product and suffix products, we can do all the approach discussed in method 3 directly onto our final answer array.

The Time Complexity would be O(n) but now, the Auxilary Space is O(1) (excluding the final answer array).

Below is the Java Code for the above algorithm.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [1] * n
        preProduct = 1

        for i in range(n):
            #initailly, when i = 0, ans[i]=1 and preProduct = 1 => 1*1 just like prefixProduct in the above solution
            ans[i] *= preProduct 
            preProduct *= nums[i]

        sufProduct = 1

        for i in range(n-1, -1, -1):
            ans[i] *= sufProduct
            sufProduct *= nums[i]
        
        return ans


# very nice solution: 

# https://leetcode.com/problems/product-of-array-except-self/solutions/1342916/3-minute-read-mimicking-an-interview

# question

# https://leetcode.com/problems/product-of-array-except-self/description/