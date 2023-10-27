import sys
sys.stdin = open('input2.txt')


def perm(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        perm(i)
        result.pop()


N, M = map(int, input().split())
result = []

perm(1)
