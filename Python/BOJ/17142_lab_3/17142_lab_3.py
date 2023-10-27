from collections import deque
from itertools import combinations as c
import sys
sys.stdin = open('input7.txt')


# 모든 바이러스는 비활성 상태
# 활성 상태가 되면 1초에 상하좌우 모든 빈칸으로 복제
# M개의 바이러스를 활성 상태로 변경
# 연구소 = NxN
# 0 = 빈칸, 1 = 벽, 2 = 바이러스 위치
# 바이러스를 모든 빈 칸에 퍼뜨리는 최소시간

# 1. 배열에서 바이러스 M개 만큼 선택하는 모든 경우의 수
# 2. BFS 돌려서 최소 시간 찾기
#   2-1. 빈칸이 없어지면 종료


def bfs(q, blank):
    visited = [[-1] * N for _ in range(N)]

    time = 0
    while True:
        length = len(q)

        if blank == 0 or length == 0:
            if blank == 0:
                return time
            else:
                return INF

        time += 1

        for i in range(length):
            x, y = q.popleft()

            if visited[x][y] == -1:
                visited[x][y] = 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == -1:
                        if lab[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
                            blank -= 1
                        elif lab[nx][ny] == 2:
                            q.append((nx, ny))
                            visited[nx][ny] = 1


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)

# 배열에서 바이러스 찾으면서 빈칸 갯수 세기
virus_position = []
blank = 0

for i in range(N):
    for j in range(N):
        if lab[i][j] == 0:
            blank += 1
        elif lab[i][j] == 2:
            virus_position.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 조합 사용해서 경우의 수 구하기
virus_comb = c(virus_position, M)

result = INF

for virus_list in virus_comb:
    q = deque()
    for virus in virus_list:
        q.append(virus)

    temp = bfs(q, blank)

    result = min(result, temp)


if result == INF:
    print(-1)
else:
    print(result)
