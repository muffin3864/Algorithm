import sys
sys.stdin = open('input1.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())

arr = [[0] * C for _ in range(R)]

if K > C * R:
    print(0)
    exit()

x, y = R - 1, 0
cnt = 1
d = 0

while True:
    if cnt == K:
        print((y+1),(R - x))
        break

    arr[x][y] = cnt
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or nx >= R or ny < 0 or ny >= C or arr[nx][ny] != 0:
        d = (d + 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    x, y = nx, ny
    cnt += 1

