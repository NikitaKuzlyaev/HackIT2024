import sys

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

v.sort(reverse=True)

p = [0 for i in range(n + 1)]
for i in range(n):
    p[i + 1] = p[i] + v[i]

q = int(sys.stdin.readline())
for i in range(q):
    d = int(sys.stdin.readline())
    l, r = 1, n

    while l <= r:
        m = (l + r) // 2
        if p[m] < d:
            l = m + 1
        else:
            r = m - 1

    sys.stdout.write(str(l) + '\n')