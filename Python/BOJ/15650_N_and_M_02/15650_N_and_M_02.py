import sys
sys.stdin = open('input2.txt')


def perm(start):
    if len(complete) == M:
        print(*complete)
        return
    else:
        for i in range(start, N + 1):
            if i not in complete:
                complete.append(i)
                perm(i + 1)
                complete.pop()


N, M = map(int, input().split())
complete = []

perm(1)

