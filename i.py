import sys


class person:
    name = ""
    prev = None
    next = None

    def __init__(self, name, prev, next):
        self.name = name
        self.prev = prev
        self.next = next
        return


def solve():
    q = int(sys.stdin.readline())

    root = person('123', None, None)
    end = person('123', None, None)
    a = person('Aaron', root, end)
    root.next = a
    end.prev = a

    persons = {'Aaron': a}

    for i in range(q):
        a = list(map(str, sys.stdin.readline().strip().split()))
        if a[1] == 'before':
            n1, n2 = a[0], a[2]
            p2 = persons[n2]
            p1 = person(n1, p2.prev, p2)
            p2.prev.next = p1
            p2.prev = p1
            persons[n1] = p1

        elif a[1] == 'after':
            n1, n2 = a[0], a[2]
            p2 = persons[n2]
            p1 = person(n1, p2, p2.next)
            p2.next.prev = p1
            p2.next = p1
            persons[n1] = p1

        elif a[0] == 'leave':
            n1 = a[1]
            p = persons[n1]
            pb = p.prev
            pa = p.next
            pb.next = pa
            pa.prev = pb

    cur = root
    while cur.next is not None:
        if cur.name != '123':
            sys.stdout.write(cur.name + "\n")
        cur = cur.next
    return


if __name__ == '__main__':
    solve()
