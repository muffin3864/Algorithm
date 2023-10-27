from collections import deque
queue = deque()
import sys
sys.stdin = open('input3.txt')
input = sys.stdin.readline


# NxM 행렬에서 0은 이동가능 1은 벽
# (1, 1)에서 시작, (N, M)의 위치까지 이동
# 이때 최단 경로를 구한다.
# 만약 이동중 벽을 K개 깨서 최단거리가 더 짧아진다면
# 벽을 K개 깨고 이동 가능
# 3차원 배열로 풀자


def bfs():
    queue.append([0, 0, K])
    visited[0][0][K] = 1

    while queue:
        x, y, z = queue.popleft()

        # 도착점에 도달하면 이동 횟수 출력
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 다음 이동이 벽이면서, 벽파괴 가능할때
                if arr[nx][ny] == 1 and z > 0 and visited[nx][ny][z-1] == 0:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1   # 이동할때 +1씩 카운트 해주기
                    queue.append((nx, ny, z - 1))   # 큐에 다가 벽을 부셨다고 표시됨

                # 다음 이동이 벽이 아니고, 한번도 방문 안한곳
                elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(N)]
# visited[x][y][0] = 벽 파괴 가능, visited[x][y][1] = 벽 파괴 불가능
# [a, b] -> a = 벽 부수기 체크용, b = 이동거리 카운트
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

print(bfs())
# print(visited)
