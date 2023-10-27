import sys
sys.stdin = open('input.txt')

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T + 1):
    cash = int(input())
    money_count = [0] * 8

    for i in range(8):
        if cash // money[i]:
            money_count[i] = cash // money[i]
            cash %= money[i]

    print(f'#{tc}')
    print(*money_count)