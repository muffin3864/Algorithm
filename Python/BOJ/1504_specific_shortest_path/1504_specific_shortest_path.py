import sys
import heapq
input = sys.stdin.readline
sys.stdin = open('input.txt')
INF = int(1e9)
# 1번 정점에서 N번 정점으로 최단거리 구하기
# 반드시 거쳐야 하는 두 정점 주어짐
# 한번 이동한 곳 다시 지나갈 수 있다
# 최단거리 출력, 경로가 없으면 -1 출력
# 1 - 2 - 3 - 4
# 1 - 3 - 2 - 4
# 1번에서 v1으로 가는 경로, v2로 가는 경로
# v1에서 v2까지의 최단 경로
# 다익스트라 써먹기
# 힙 쓰면 데이터 값이 가장 낮은것을 우선으로 정렬


N, E = map(int, input().split())    # N = 정점개수, E = 간선개수
graph = [[] for _ in range(N + 1)]

# 방향성이 없으니깐 a,b 일때와 b, a일때 모두 추가해준다.
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())  # v1, v2 = 반드시 거쳐야 하는 정점


def search(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + next[1]

            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance


# 1번에서 N까지 [1000000000, 0, 3, 5, 4]
N_distance = search(1)

# v1일때 [1000000000, 3, 0, 3, 4]
v1_distance = search(v1)

# v2일때 [1000000000, 5, 3, 0, 1]
v2_distance = search(v2)

# v1를 먼저 들릴때
path_v1 = N_distance[v1] + v1_distance[v2] + v2_distance[N]

# v2를 먼저 들릴때
path_v2 = N_distance[v2] + v2_distance[v1] + v1_distance[N]

# 둘 중 작은 값 출력
result = min(path_v1, path_v2)

if result >= INF:
    print(-1)
else:
    print(result)