s1, *n1 = map(str, input().split())
t1 = 0
if s1 == "hurry":
    t1 = -int(n1[0])
elif s1 == "late":
    t1 = int(n1[0])

s2, *n2 = map(str, input().split())
t2 = 0
if s2 == "hurry":
    t2 = -int(n2[0])
elif s2 == "late":
    t2 = int(n2[0])

if t1 == t2:
    print("together")
elif t1 < t2:
    print("Chipy-chipy", (t2 - t1))
else:
    print("Chapa-chapa", (t1 - t2))
