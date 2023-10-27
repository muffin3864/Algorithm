import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 트리의 개수를 세는 프로그램
# 트리인지 확인 하려면 한바퀴 돌아오는지 확인 해보면 됨

# start 노드부터 시작하여 BFS를 사용해서 끝까지 돌고
# 다시 돌아와 지는지 확인
def Cycle(start):
    is_Cycle = False
    q = deque()
    q.append(start)
    # 큐에서 노드를 뽑을때마다 visited 갱신
    # 만약 뽑은 노드의 visited가 이미 1이라면 사이클이 존재
    # 1-2, 2-3, 3-1을 가정하면
    # 3-1 을 갈때 이미 1에는 갱신이 되있으므로 사이클이 돌아가는 것
    while q:
        cnt_node = q.popleft()

        if visited[cnt_node]:
            is_Cycle = True

        visited[cnt_node] = 1

        for adj_node in graph[cnt_node]:
            if visited[adj_node] == 0:
                q.append(adj_node)

    return is_Cycle


n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    count = 0

    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for node in range(1, n + 1):
        if visited[node] == 0:
            if not Cycle(node):  # 사이클이 도는지 체크해서 돌지 않는다면 카운트 +1
                count += 1

    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')
    print(graph)
    case += 1
    n, m = map(int, input().split())

