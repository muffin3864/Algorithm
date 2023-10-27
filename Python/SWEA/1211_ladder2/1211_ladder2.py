import sys
sys.stdin = open('input.txt')


# 내려가다 양쪽에 1이있으면 그곳으로 이동
dx = [1, 0, 0]
dy = [0, 1, -1]

def search(x, y):
    arr = [[0] * 100 for _ in range(100)]

    arr[x][y] = 1

    cnt = 0

    while x != 99:
        for k in range(3):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] and arr[nx][ny] == 0:
                x, y = nx, ny
                arr[x][y] = 1
                cnt += 1

    if arr[99][y] == 1:
        return cnt


# 모든 출발점 다 출발 시켜서 최단 거리인 출발점 구하기

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_count = []
    # 출발점 찾고 시작점으로 지정
    for i in range(100):
        if ladder[0][i] == 1:
            result = search(0,i)

            min_count.append([result,i])

    min_count.sort()

    print(f'#{tc} {min_count[0][1]}')
