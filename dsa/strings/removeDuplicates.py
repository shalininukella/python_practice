# Here’s a well-defined coding question for **removing duplicates from a string**, which is a common interview-style prompt.
# ### 💬 **Question: Remove Duplicates from String**
# Write a function that takes a string as input and returns a new string with **all duplicate characters removed**, preserving the **original order** of characters.
# ### ✍️ **Function Signature:**

# ```python
# def removeDuplicates(s: str) -> str:
# ```

# ---

# ### 🔹 **Input:**

# * A string `s` containing English letters, digits, or symbols.

# ---

# ### 🔹 **Output:**

# * A string with duplicates removed, keeping only the **first occurrence** of each character.

# ---

# ### ✅ **Constraints:**

# * `0 <= len(s) <= 10^5`
# * The input string may contain **any printable ASCII characters**.
# * Comparisons are **case-sensitive** (i.e., `'A'` and `'a'` are different).

# ---

# ### 🧪 **Examples:**

# #### Example 1:

# ```python
# Input: "banana"
# Output: "ban"
# # Explanation: Keep the first 'b', 'a', 'n'; ignore repeated 'a' and 'n'
# ```

# #### Example 2:

# ```python
# Input: "abcabcabc"
# Output: "abc"
# ```

# #### Example 3:

# ```python
# Input: "AaBbCc"
# Output: "AaBbCc"
# # Explanation: No duplicates due to case sensitivity
# ```

# #### Example 4:
# Input: ""
# Output: ""

#set
def removeDuplicates(s: str) -> str:
    seen = set()
    res = []

    for c in s:
        if c not in seen:
            seen.add(c)
            res.append(c)

    final = "".join(res)
    return final 

