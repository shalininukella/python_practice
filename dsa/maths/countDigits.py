def countDigits(n: int) -> int:
    cnt = 0
    temp = n
    while n>0:
        x = n%10
        if x != 0 and temp%x == 0:
            cnt = cnt + 1
        n = n//10
    return cnt

# https://www.naukri.com/code360/problems/count-digits_8416387