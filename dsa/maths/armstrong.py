def checkArmstrong(n):
    #write your code here !!!!!!!!!
    if n <= 0: 
        return False
    elif n>0 and n<10:
        return True

    temp = n
    cnt = 0 
    
    while temp > 0:
        temp //= 10
        cnt += 1

    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit**cnt
        temp //= 10
    
    if sum == n:
        return True
    else:
        return False

# https://www.naukri.com/code360/problems/check-armstrong_589?leftPanelTabValue=SUBMISSION