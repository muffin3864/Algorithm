import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())    # V = 정점 개수, E = 간선개수
K = int(input())    # 시작점
graph = [[] for _ in range(V + 1)]  # 양방향으로
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def search(start):
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


search(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])