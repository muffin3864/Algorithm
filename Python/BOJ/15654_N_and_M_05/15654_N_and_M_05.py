import sys
sys.stdin = open('input3.txt')


def perm(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        if nums[i] not in result:
            result.append(nums[i])
            perm(i)
            result.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []

perm(0)
