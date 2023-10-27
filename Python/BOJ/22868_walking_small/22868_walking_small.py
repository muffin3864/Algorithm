from collections import deque
import sys
sys.stdin = open('input.txt')

# S에서 출발, E를 찍고 다시 S로 돌아오는 경로
# 방문한 정점은 재방문 X
# S에서 E갈때 가장 짧은 거리, E에서 S갈때 가장 짧은 거리
# 짧은거리의 경로가 여러개 나올때는 숫자가 빠른 것을 선택
# S-E + E-S


def go(x):
    q.append((x, [x]))

    while q:
        x, path = q.popleft()

        if x == E:
            for x in path:
                result.append(x)
            return

        for y in roads[x]:
            if visited[y] == -1:
                visited[y] = 1
                q.append((y, path + [y]))


def come(x):
    q.append((x, [x]))

    while q:
        x, path = q.popleft()

        if x == S:
            for x in path:
                result.append(x)
            return

        for y in roads[x]:
            if visited[y] == -1:
                visited[y] = 1
                q.append((y, path + [y]))


N, M = map(int, input().split())    # N: 정점개수, M: 도로의 개수

roads = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    # 순번이 1번 부터 이므로 1씩 빼주기
    A -= 1
    B -= 1
    roads[A].append(B)
    roads[B].append(A)

for i in range(N):
    roads[i].sort()

S, E = map(int, input().split())
S -= 1
E -= 1

result = []

# 처음 출발할때
visited = [-1] * N
visited[S] = 1
q = deque()

go(S)

# 다시 돌아올때
visited = [-1] * N
for i in result:    # result를 순회하면서 방문 했던곳 찍어주기
    visited[i] = 1
visited[S] = -1     # 도착지점도 갈 수 있게 초기화
q = deque()

come(E)

print(len(result) - 2)
