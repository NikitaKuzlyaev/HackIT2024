import sys

n = int(sys.stdin.readline())
s = str(sys.stdin.readline().strip())

mx, cur = 1, 1

for i in range(1, n):
    if s[i] != s[i - 1]:
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1

print(mx)
