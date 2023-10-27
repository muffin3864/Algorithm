import sys
sys.stdin = open('input2.txt')

# 2x2가 되면 제거됨
# 계속 반복하다가 넴모를 없애고 싶은데 못 없애면 게임 끝
# 게임을 그만 두었을때 넴모의 배치 가짓수 출력

N, M = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
result = 0


def dfs(x, y):
    global result
    # 종료 조건
    if (x, y) == (1, N + 1):
        result += 1
        return

    # 새로운 좌표값 넣기
    if x == M:
        nx = 1
        ny = y + 1
    else:
        nx = x + 1
        ny = y

    # 비어있으면 방문기록 남기고 재귀 ㄱㄱ
    if graph[y - 1][x] == 0 or graph[y - 1][x - 1] == 0 or graph[y][x - 1] == 0:
        graph[y][x] = 1
        dfs(nx, ny)
        # 재귀 돌고 나오면서 초기화
        graph[y][x] = 0

    dfs(nx, ny)


dfs(1, 1)

print(result)
