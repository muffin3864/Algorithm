import sys
sys.stdin = open('input.txt')

# 50000, 10000, 5000, 1000, 500, 100, 50, 10
# [0, 0, 0, 0, 0, 0, 0, 0] 인덱스 위치마다 다른 금액


T = int(input())

for tc in range(1, T + 1):

    cash = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8

    for i in range(8):
        if cash // money[i]:
            change[i] = cash // money[i]
            cash %= money[i]

    print(f'#{tc}')
    print(*change)