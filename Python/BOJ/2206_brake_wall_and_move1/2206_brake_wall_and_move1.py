import sys
sys.stdin = open('input1.txt')

from collections import deque

# NxM 행렬에서 0은 이동가능 1은 벽
# (1, 1)에서 시작, (N, M)의 위치까지 이동
# 이때 최단 경로를 구한다.
# 만약 이동중 벽을 1개 깨서 최단거리가 더 짧아진다면
# 벽을 1개 깨고 이동 가능


def bfs(start_x, start_y, start_z):
    queue = deque()
    queue.append((start_x, start_y, start_z))

    while queue:
        x, y, z = queue.popleft()

        # 도착점에 도달하면 이동 횟수 출력
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 다음 이동이 벽이면서, 벽파괴 가능할때
            if arr[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1   # 이동할때 +1씩 카운트 해주기
                queue.append((nx, ny, 1))   # 큐에 다가 벽을 부셨다고 표시됨

            # 다음 이동이 벽이 아니고, 한번도 방문 안한곳
            elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# visited[x][y][0] = 벽 파괴 가능, visited[x][y][1] = 벽 파괴 불가능
# [a, b] -> a = 벽 부수기 체크용, b = 이동거리 카운트
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

#[
# [[1, 3], [0, 2], [0, 3], [0, 4]],
# [[0, 2], [0, 0], [0, 0], [0, 5]],
# [[0, 0], [0, 8], [0, 7], [0, 6]],
# [[0, 10], [0, 9], [0, 8], [0, 7]],
# [[0, 11], [0, 0], [0, 0], [0, 0]],
# [[0, 12], [0, 13], [0, 14], [0, 15]]
# ]

print(bfs(0, 0, 0))
print(visited)
