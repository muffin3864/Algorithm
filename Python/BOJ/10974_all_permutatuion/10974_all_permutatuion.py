import sys
sys.stdin = open('input.txt')


N = int(input())
arr = [i for i in range(1, N + 1)]
permutation = [0] * N
visited = [0] * N


def perm(r, K):
    if r == K:
        print(*permutation)
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                permutation[r] = arr[i]
                visited[i] = 1
                perm(r + 1, K)
                visited[i] = 0


perm(0, N)
