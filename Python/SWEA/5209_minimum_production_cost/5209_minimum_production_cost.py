import sys
sys.stdin = open('input.txt')

# 각 제품의 공장별 생산비용이 주어짐
# 각 공장별 생산 비용을 다 더한값이 최소가 되도록 출력


def perm(r, acc):
    global result
    # 시간 초과 해결하기 위해 가지치기
    if acc > result:
        return
    # 종료 조건
    if r == N:
        if acc < result:
            result = acc
        return
    # 재귀
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(r+1, acc + cost[r][i])
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    result = sum(sum(cost, []))
    visited = [0] * N
    perm(0, 0)

    print(f'#{tc} {result}')
