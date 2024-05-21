n = int(input())


res = 0
for i in range(1, n + 1):
    t = (n - 1) // i

    if i > t:
        res -= (i - 1) ** 2
        break
    elif i == t:
        res += t * 2
        res -= t ** 2
        break

    res += t * 2

print(res)