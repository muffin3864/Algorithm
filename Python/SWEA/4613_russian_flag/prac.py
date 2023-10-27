import sys
sys.stdin = open('input.txt')

# 최소 1줄 이상 칠해야 됨

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    change = []
    for row in flag:
        w = M - row.count('W')
        b = M - row.count('B')
        r = M - row.count('R')
        change.append([w, b, r])

    result = 99999

    for w in range(0, N - 3 + 1):
        pass
