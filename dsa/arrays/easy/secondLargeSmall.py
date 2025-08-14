def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    maxi = secondMax = float('-inf')
    small = secondSmall = float('inf')
    for i in a:
        if i > maxi:
            secondMax = maxi
            maxi = max(maxi, i)

        elif i > secondMax and i < maxi:
            secondMax = i

        if i < small:
            secondSmall = small
            small = min(small, i)
            
        elif i < secondSmall and i > small:
            secondSmall = i

    return [secondMax, secondSmall]

# https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960?leftPanelTabValue=SUBMISSION