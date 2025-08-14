from  typing import *

def printNtimes(n: int) -> List[str]:
    if n <=1:
        return ["Coding Ninjas"]
    namesList = printNtimes(n-1)
    namesList.append("Coding Ninjas")
    return namesList

# https://www.naukri.com/code360/problems/-print-n-times_8380707?leftPanelTabValue=SUBMISSION

# # c++

# vector<string> printNTimes(int n) {
# 	// Write your code here.
# 	if(n<=1){
# 		return {"Coding Ninjas"};
# 	}
# 	vector<string> names;
# 	names = printNTimes(n-1);
# 	names.push_back("Coding Ninjas");
# 	return names;
# }