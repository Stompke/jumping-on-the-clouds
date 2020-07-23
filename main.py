# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

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