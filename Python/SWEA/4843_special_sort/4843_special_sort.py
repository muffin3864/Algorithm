import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    arr.sort()

    while len(result) != N:
        result.append(arr.pop(-1))
        result.append(arr.pop(0))
        if len(result) == 10:
            break

    print(f'#{tc}', *result)