from bz2 import compress


def stringCompress(strs):
    compressed = ''
    cnt = 1

    for i in range(1, len(strs)):
        if strs[i] == strs[i-1]:
            cnt += 1
        else:
            #when they are not equal
            if cnt > 1:
                compressed += strs[i-1] + str(cnt)
            else:
                compressed += strs[i-1]
            cnt = 1

    #for last word
    if cnt > 1:
        compressed += strs[-1] + str(cnt)
    else:
        compressed += strs[-1]

    return compressed

print(stringCompress('abbbbbbbbbbbccd'))


