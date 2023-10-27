import sys
sys.stdin = open('input.txt')

def search_cross(x, y):
    cnt = arr[x][y]
    for plus in range(1,M):
        for k in range(4):
            nx = x + dx[k] * plus
            ny = y + dy[k] * plus
            if 0 <= nx < N and 0 <= ny < N:
                cnt += arr[nx][ny]
    return cnt


def search_diagnol(x, y):
    cnt = arr[x][y]
    for plus in range(1, M):
        for k in range(4):
            nx = x + dk[k] * plus
            ny = y + dl[k] * plus
            if 0 <= nx < N and 0 <= ny < N:
                cnt += arr[nx][ny]
    return cnt


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dk = [-1, 1, 1, -1]
dl = [1, 1, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    kill = []
    for x in range(N):
        for y in range(N):
            cross = search_cross(x, y)
            diagnol = search_diagnol(x, y)

            if cross >= diagnol:
                kill.append(cross)
            else:
                kill.append(diagnol)

    print(f'#{tc} {max(kill)}')