import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    start, end = N // 2, N // 2
    # 가운데 행 에서부터 시작

    sum_harvest = 0
    for i in range(N):
        for j in range(start, end + 1):
            sum_harvest += farm[i][j]
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{tc} {sum_harvest}')