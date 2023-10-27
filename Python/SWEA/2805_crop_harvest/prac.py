import sys
sys.stdin = open('input.txt')

# 농장의 넓이 만큼의 수입 구하기
# 농장의 크기는 항상 홀수
# 마름모 꼴로만 수확
# 마름모 안에 들어가는 배열의 숫자들을 모두 더함

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start, end = N // 2, N // 2

    sum_harvest = 0
    for i in range(N):
        for j in range(start, end+1):
            sum_harvest += arr[i][j]
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{tc} {sum_harvest}')
