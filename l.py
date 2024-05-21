import sys

n, d = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

w = []
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    w.append([a, b])

w.sort()
res = 0

for a, b in w:
    can_do = d // b
    if can_do >= n:
        res += n * a
        print(res)
        break
    n -= can_do
    res += a * can_do
else:
    print(-1)
