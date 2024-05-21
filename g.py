import sys

n = int(sys.stdin.readline())
a = list(map(str, sys.stdin.readline().split()))

r, s, p = [a.count(i) for i in "RSP"]

win_r = 1 << 60 if (r == 0 or s == 0 and p != 0) else n - r + p
win_s = 1 << 60 if (s == 0 or p == 0 and r != 0) else n - s + r
win_p = 1 << 60 if (p == 0 or r == 0 and s != 0) else n - p + s

print(min(win_r, win_s, win_p))