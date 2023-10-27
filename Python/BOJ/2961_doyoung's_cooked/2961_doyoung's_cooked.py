import sys
sys.stdin = open('input2.txt')

# 재료 N개
# 신맛 S, 쓴맛 B
# 음식의 신맛은 재료의 신맛의 곱, 쓴맛은 합
# 신맛과 쓴맛의 차이가 가장 작은 요리 출력

N = int(input())
# ingredient[i][j] =>   j = 0 : 신맛, j = 1 : 쓴맛
ingredient = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)

for i in range(1, 1 << N):
    s = 1
    b = 0
    for j in range(N):
        if i & (1 << j) != 0:
            s *= ingredient[j][0]
            b += ingredient[j][1]
    ans = min(ans, abs(s-b))
print(ans)
