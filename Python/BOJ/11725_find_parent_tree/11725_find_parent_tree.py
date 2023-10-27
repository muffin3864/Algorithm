# import sys
# input = sys.stdin.readline
# # sys.stdin = open('input2.txt')
# from collections import deque

# # 트리의 루트를 1이라 정했을 때, 각 노드의 부모를 구하기
# # 각 노드의 부모 노드 번호를 2번 노드부터 출력

# N = int(input())
# graph = [[] for _ in range(N + 1)]

# # 양방향으로 데이터를 주어서 양방향으로 다 받아서 리스트에 넣기
# for _ in range(N-1):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# # print(graph)
# distance = [0] * (N+1)  # 노드 이동할때 마다 이전 노드를 기록

# def bfs():
#     q = deque()
#     q.append(1)
    
#     while q:
#         now = q.popleft()

#         for next in graph[now]:
#             if distance[next] == 0: # 방문한적 없으면 기록
#                 distance[next] = now
#                 q.append(next)

# bfs()
# result = distance[2::]  # 2번 노드부터 출력

# for i in result:
#     print(i)



# 지수 코드s

import sys
input = sys.stdin.readline


N = int(input())


Trees = [[] for _ in range(N-1)]
print(Trees)
for _ in range(N-1):
    node1, node2 = map(int,input().split())
    if node1 == 1:
        Trees[node2-2].append(node1)
    elif node2 == 1:
        Trees[node1-2].append(node1)
    elif Trees[node2-2] != False:
        Trees[node2-2].append(node1)
print(Trees)