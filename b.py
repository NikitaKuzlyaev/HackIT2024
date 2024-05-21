n, m = map(int, input().split())

dp = [0 for i in range(m + 1)]
dp[n] = 1

res = 0

for bet in range(1, m + 3):
    new_dp = [0 for i in range(m + 1)]
    for i in range(m):
        if i + bet >= m:
            res += dp[i] / 2
        if i + bet < m:
            new_dp[i + bet] += dp[i] / 2
        if i - bet >= 0:
            new_dp[i - bet] += dp[i] / 2

    for i in range(m + 1):
        dp[i] = new_dp[i] * 1

print("%.16f" % res)
