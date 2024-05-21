import sys

n = int(sys.stdin.readline())
a = list(map(str, sys.stdin.readline().split()))
b = list(map(str, sys.stdin.readline().split()))

f = {}

for i in range(n):
    f[a[i]] = f[a[i]] + 1 if a[i] in f else 1
    f[b[i]] = f[b[i]] - 1 if b[i] in f else -1

u, v = -1, -1
for key in f:
    if f[key] == 1:
        u = key
    elif f[key] == -1:
        v = key

print(u, v)