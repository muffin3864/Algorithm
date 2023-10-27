import sys
from collections import deque
sys.stdin = open('input.txt')

# 지훈이와 불은 매 분마다 한칸씩 이동
# 불은 각 지점에서 네 방향으로 확산
# '#' : 벽
# '.' : 지나갈 수 있는 공간
# 'J' : 지훈이 초기 위치
# 'F' : 불이 난 공간
# 탈출 못 하면 IMPOSSIBLE 출력
# 가장 빠른 탈출 시간 출력
# BFS 로 불이 움직일때 지훈이가 움직일때 각각 체크해야한다.

T = int(input())
for tc in range(T):
    C, R = map(int, input().split())
    graph = []
    q = deque()

    # 그래프 값 받으면서 지훈이 위치 큐에 추가
    for i in range(R):
        graph.append(list(input()))
        if '@' in graph[i]:
            q.append((0, i, graph[i].index('@')))

    # 불 시작점 찾아서 큐에 추가
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '*':
                q.append((-1, i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 'IMPOSSIBLE'

    while q:
        time, x, y = q.popleft()

        # 조건에 따른 탈출시간 출력
        if time >= 0 and graph[x][y] != '*' and (x == 0 or y == 0 or x == R - 1 or y == C - 1):
            result = time + 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#':

                # 지훈이 탈출
                if time >= 0 and graph[nx][ny] == '.':
                    graph[nx][ny] = '@'
                    q.append((time + 1, nx, ny))

                # 불 번지기 ( 불은 시간과 관계없이 지훈이가 움직이고 나서 무조건 번지므로 -1로 고정시킨다)
                if time == -1 and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    q.append((-1, nx, ny))
    print(result)
