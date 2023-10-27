import sys
sys.stdin = open('input2.txt')

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열


def perm():
    if len(complete) == M:
        print(' '.join(map(str, complete)))
        return

    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        complete.append(i)
        perm()
        complete.pop()
        visited[i] = False


N, M = map(int, input().split())
visited = [0] * (N+1)
complete = []

perm()
