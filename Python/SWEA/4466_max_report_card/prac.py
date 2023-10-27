import sys
sys.stdin = open('input.txt')
# N개의 시험
# 성적표에 K개 넣음
# 총점이 최대일때 총점

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    score.sort()
    score.reverse()

    sum_score = sum(score[0:K])


    print(f'#{tc} {sum_score}')

