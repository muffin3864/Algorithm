import sys
sys.stdin = open('input3.txt')


def perm(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        perm(i)
        result.pop()


N, M = map(int, input().split())
result = []

perm(0)
