def jumpingOnClouds(c):
    print(c)
    count = 0
    cur = 0
    while cur < len(c)-3:
        if c[cur+2] == 0:
            count += 1
            cur = cur + 2
        else:
            count += 1
            cur = cur + 1
    count += 1
    return count