import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    sum_list = []
    for i in range(N - M + 1):
        sum_num = []
        for j in range(M):
            sum_num.append(arr[i+j])
        sum_list.append(sum(sum_num))

    result = max(sum_list) - min(sum_list)

    print(f'#{tc} {result}')