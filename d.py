from copy import deepcopy

states = []
for a in [0, 1, 2]:
    for b in [0, 1, 2]:
        for c in [0, 1, 2]:
            if a + b + c != 0:
                states.append([a, b, c])


def r(f, s, cur_t, need_t):
    delta_t_min = 1 << 60
    for i in range(3):
        if f[i] > 0 and s[i] > 0:
            delta_t_min = min(f[i] / s[i], delta_t_min)
    if cur_t + delta_t_min == need_t:
        return True
    if cur_t + delta_t_min > need_t:
        return False
    if delta_t_min == 1 << 60:
        return False

    nf = deepcopy(f)
    for i in range(3):
        if nf[i] > 0 and s[i] > 0:
            nf[i] -= delta_t_min * s[i]

    flag = False
    for state in states:
        st = state * 1
        flag = flag or r(nf, st, cur_t + delta_t_min, need_t)
    return flag


a, b, c = map(int, input().split())
t = int(input())

flag = False
for state in states:
    flag = flag or r([a, b, c], state, 0, t)

print("Yes" if flag else "No")
