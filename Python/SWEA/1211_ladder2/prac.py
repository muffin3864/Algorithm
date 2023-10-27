import sys
sys.stdin = open('input.txt')

def search(x, y):
    visited = [[0] * 100 for _ in range(100)]

    visited[x][y] = 1
    cnt = 0
    while x != 99:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and ledder[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                x, y = nx, ny
                cnt += 1

    if ledder[99][y] == 1:
        return cnt


dx = [1, 0, 0]
dy = [0, -1 , 1]

for _ in range(10):
    tc = int(input())
    ledder = [list(map(int, input().split())) for _ in range(100)]
    min_count = []
    # 출발점 찾기
    for y in range(100):
        if ledder[0][y] == 1:
            result = search(0, y)
            min_count.append([result, y])
    min_count.sort()

    print(f'#{tc} {min_count[0][1]}')