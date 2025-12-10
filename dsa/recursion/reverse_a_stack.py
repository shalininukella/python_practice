# Time Complexity: O(n²), as each element is popped and inserted at the bottom (O(n) per element).
# Space Complexity: O(n), as only the recursion stack is used.

class Solution:
    def pushBottom(self, stack, val):
        #base
        if not stack:
            stack.append(val)
            return
            
        #else remove the topmost element and send the rest of the stack to the next recursive depth function
        x = stack.pop()

        # Recursively push val to the bottom
        self.pushBottom(stack, val)

        #when the resursive function in which we previously entered is exited then it will come to this line, so since we removed the top element popping, we must push it again since we have pushed the topmost ele to the bottom 
        stack.append(x)

    def reverseStack(self, stack):
        # Base case: empty stack
        if not stack:
            return
        
        # Pop top
        top_val = stack.pop()

        # Reverse smaller stack
        self.reverseStack(stack)

        # Insert at bottom
        self.pushBottom(stack, top_val)
        
    
# https://takeuforward.org/plus/dsa/problems/reverse-a-stack