#cpp
#tle
# long long factorial(long long n){
#     int fact = 1;
#     for(int i=1; i<=n ;i++){
#         fact *= i;
#     }
#     return fact;
# }

# vector<long long> factorialNumbers(long long n) {
#     // Write Your Code Here
#     vector<long long> ans;
#     int x = 1;
#     int i = 1;
#     while(x <= n && i <= n){
#         ans.push_back(x);
#         x = factorial(++i);
#     }
#     return ans;
# }


#without recursion
from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    res = []
    i = 1
    fact = 1
    while fact <= n:
        res.append(fact)
        i += 1
        fact *= i
    return res

# https://www.naukri.com/code360/problems/factorial-numbers-not-greater-than-n_8365435?leftPanelTabValue=SUBMISSION