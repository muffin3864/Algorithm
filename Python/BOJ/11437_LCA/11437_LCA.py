from collections import deque
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(int(1e5))
# N개의 정점으로 이루어진 트리
# 각 정점은 1부터 N번까지 번호가 매겨짐
# 루트는 1번
# 두 노드의 쌍이 주어졌을때, 두 노드의 가장 가까운 조상이 몇 번인지 출력


def bfs(s):
    q = deque()
    q.append(s)
    while q:
        node = q.popleft()
        visited[node] = 1
        for i in tree[node]:
            if visited[i] == 0:
                level[i] = level[node] + 1
                parent[i] = node
                q.append(i)


def LCA(a, b):
    # 두 노드의 level이 다를 경우 level 맞추기
    while level[a] != level[b]:
        if level[a] > level[b]:
            a = parent[a]
        else:
            b = parent[b]

    # level이 같을때, 부모 찾기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


N = int(input())
parent = [0] * (N + 1)  # 그 정점의 조상 기록
level = [0] * (N + 1)   # 공통된 level
visited = [0] * (N + 1) # 방문 기록

# 양방향으로 입력 받기
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

# 트리의 깊이와 부모 리스트 만들기
bfs(1)
# print(parent)
# print(level)


# 노드값 입력 받으면서 공통 조상 찾기
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
