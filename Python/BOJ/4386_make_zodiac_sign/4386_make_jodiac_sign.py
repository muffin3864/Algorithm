import math
import sys
sys.stdin = open('input.txt')

# n개의 별들을 이어 별자리를 1개 만든다
# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태
# 모든 별들은 선을 통해 직/간접적으로 이어져 있어야 한다.
# 선을 하나 이을 때마다 거리만큼의 비용이 든다
# 최소비용 출력
# 크루스칼 알고리즘 사용하자


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n + 1)]
stars = []
edges = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge

    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += cost

print(round(result, 2))
