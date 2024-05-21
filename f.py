import time as bomb
import random as pin
import sys


def solve():
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    w = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    d = set(map(int, sys.stdin.readline().split()))

    child = [[] for i in range(n)]
    for i in range(1, n):
        child[p[i] - 1].append(i)

    # какой ответ на задачу, если у нас все дерево --- поддерево с вершины i
    ans = [0 for i in range(n)]

    # вес поддерева вершины i
    sub_tree_cost = [0 for i in range(n)]

    # есть ли в поддереве вершины i хотя бы одна особенная вершина
    sub_tree_with_d = [False for i in range(n)]

    # порядок в котором смотрим вершины (от листьев к предкам, от предка к предку и т.д.)
    order = [0]

    it = 0
    while it < len(order):
        f = order[it]
        it += 1
        for u in child[f]:
            order.append(u)

    for u in order[::-1]:

        sub_tree_cost[u] = w[u]
        sub_tree_with_d[u] = (u + 1) in d
        for v in child[u]:
            sub_tree_cost[u] += sub_tree_cost[v]
            sub_tree_with_d[u] = sub_tree_with_d[u] or sub_tree_with_d[v]

        if u + 1 in d:
            ans[u] = sub_tree_cost[u]
            continue

        res = 0
        for v in child[u]:
            if sub_tree_with_d[v] or ans[v] < 0:
                res += ans[v]

        ans[u] = min(res, sub_tree_cost[u])

    sys.stdout.write(str(ans[0]) + "\n")
    return


if __name__ == '__main__':
    solve()
