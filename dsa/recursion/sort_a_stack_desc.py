# Time Complexity: O(n2), where n is the number of elements in the stack.
# Space Complexity: O(n), due to the recursion stack.

class Solution:
    def compareTopAndSwapIf(self, stack, val):
        #base
        if not stack or val >= stack[-1]:
            stack.append(val)
            return

        #update the stack by removing the topmost ele
        x = stack.pop() #this x will be preserved in recursive function, so don't worry to pop

        #recursively go deep till we get an empty stack to append the val(which is the actual topmost ele which is coming from the function sortStack)
        self.compareTopAndSwapIf(stack, val)

        stack.append(x)

    def sortStack(self, stack):
        # Your code goes here
        #base case
        if not stack:
            return

        top_val = stack.pop()#will be preserved in this function

        #recursively go deep till we get an empty stack
        self.sortStack(stack)

        self.compareTopAndSwapIf(stack, top_val)


# https://takeuforward.org/plus/dsa/problems/sort-a-stack