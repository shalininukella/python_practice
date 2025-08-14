from typing import List

def printNos(x: int) -> List[int]: 
    # Write your code here
    if x == 1:
        return [1]
    numList = printNos(x-1)
    numList.append(x)
    return numList


# C++ 
# vector<int> printNos(int x) {
#     // Write Your Code Here
#     if(x==1) return {1};
#     vector<int> numList;
#     numList = printNos(x-1);
#     numList.push_back(x);
#     return numList;
# }

# https://www.naukri.com/code360/problems/print-1-to-n_628290?leftPanelTabValue=PROBLEM