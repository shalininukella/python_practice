# Time Complexity: O(log (n/2)) +  O(log (n/2)) or O(log (n+1)/2)) = O(log n)
        # myPow(5, evens, MOD) → O(log n)
        # myPow(5, evens, MOD) → O(log n)

        # because:
        #     log(n/2​)=logn−log2, ignore log n =>  log(n/2​)=logn

# Space Complexity: O(1)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        # Custom Power Function: (base^exp) % mod
        # Time Complexity: O(log exp)
        def myPow(x, exp, MOD):
            ans = 1
            while (exp > 0):

                # If exp is odd, multiply result with base
                if (exp & 1) != 0:
                    ans *= x

                # Square the base and halve the exponent
                x = (x * x) % MOD
                exp = exp // 2
            
            return ans 

        # 1. Calculate how many even and odd positions we have
        odds = n // 2
        evens = (n+1) // 2 # or n - odds

        # 2. Calculate 5^(even_places) and 4^(odd_places) efficiently
        res = (myPow(5, evens, MOD) * myPow(4, odds, MOD)) % MOD

        return res
# https://leetcode.com/problems/count-good-numbers/submissions/1851084679/