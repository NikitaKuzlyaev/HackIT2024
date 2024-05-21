aa = list(map(int, input().split()))
a = aa + aa + aa

for i in range(14):
    x, y, z = a[i], a[i + 1], a[i + 2]

    if x * y + y * z < x * z:
        print("Non-convex")
        break
else:
    print("Convex")
