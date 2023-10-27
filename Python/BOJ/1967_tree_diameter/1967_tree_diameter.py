import sys
sys.stdin = open('input.txt')

# 임의의 노드 2개 사이의 간선의 합이 가장 큰거 찾기
# 트리의 끝 부분들만 잡아 당겨짐
# 한 끝점에서 다른 모든 끝점으로 가는 경우의 수를 생각하면 간선의 합 계산

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n - 1)]

