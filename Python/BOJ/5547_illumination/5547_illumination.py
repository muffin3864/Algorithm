from collections import deque
import sys
sys.stdin = open('input1.txt')

# 변의 길이 1m인 정육각형, 벽의 총 길이 64미터
# 건물 외각에만 조명 장식
# 건물은 1, 없으면 0
# 지도 가장 왼쪽 위는 (1, 1)
# (x, y) 오른쪽 좌표는 (x+1, y)
# y가 홀수이면, 아래쪽에 있는 좌표는 (x, y + 1)
# y가 짝수이면, 오른쪽 아래에 있는 좌표는 (x, y + 1)
# 조명을 장식하는 벽면의 길이 합 출력

W, H = map(int, input().split())
graph = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(1, H + 1):
    graph[i][1 : W + 1] = map(int, input().split())


dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]   # 짝수 홀수 나눠서


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    visited[y][x] = 1
    length = 0

    while q:
        y, x = q.popleft()

        for k in range(6):
            ny = y + dy[k]
            nx = x + dx[y % 2][k]

            if 0 <= ny < H + 2 and 0 <= nx < W + 2:
                if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                elif graph[ny][nx] == 1:
                    length += 1

    return length


print(bfs(0, 0))
