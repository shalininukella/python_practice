# https://leetcode.com/problems/reverse-string/submissions/1736185325/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        

# Reversing a string in Python is simple and can be done in multiple ways. Here's the most common and Pythonic way:

# ---

# ### ✅ **1. Using Slicing** (Best way)

# ```python
# s = "hello"
# reversed_s = s[::-1]
# print(reversed_s)  # Output: "olleh"
# ```

# * `s[::-1]` means: start from end to beginning, stepping backwards by 1.

# ---

# ### ✅ **2. Using `reversed()` and `join()`**

# ```python
# s = "hello"
# reversed_s = ''.join(reversed(s))
# print(reversed_s)  # Output: "olleh"
# ```

# * `reversed()` returns an iterator, and `join()` stitches it back into a string.

# ---

# ### ✅ **3. Using a Loop** (Educational, not recommended for production)

# ```python
# s = "hello"
# reversed_s = ''
# for char in s:
#     reversed_s = char + reversed_s
# print(reversed_s)  # Output: "olleh"
# ```

# * This works, but is inefficient for long strings due to repeated string concatenation.

# ---

# ### Summary:

# | Method       | Syntax                 | Recommended |
# | ------------ | ---------------------- | ----------- |
# | Slicing      | `s[::-1]`              | ✅ Yes       |
# | `reversed()` | `''.join(reversed(s))` | ✅ Yes       |
# | Loop         | Manual reversal        | ❌ No (slow) |

# Let me know if you want to reverse **words** instead of characters.
 