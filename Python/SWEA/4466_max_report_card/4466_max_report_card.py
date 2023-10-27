import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    score.sort()
    score.reverse()

    sum_score = 0
    for i in range(K):
        sum_score += score[i]

    print(f'#{tc} {sum_score}')