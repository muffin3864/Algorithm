import heapq
import sys
# input = sys.stdin.readline
sys.stdin = open('input1.txt')
INF = int(1e9)
# 1번 부터 N번 까지 M개의 단방향 도로 (모든 도로의 거리는 1)
# 도시 X에서 출발해서 최단거리가 K인 도시 모두 출력(X에서 X로 가는 거리는 항상 0)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N + 1)


for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


def search(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + 1

            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
    return distance


result = search(X)

if result.count(K) != 0:
    print(result.index(K))
else:
    print(-1)