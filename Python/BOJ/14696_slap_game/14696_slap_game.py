import sys
sys.stdin = open('input.txt')

# 별 > 동그라미 > 네모 > 세모 순서로 갯수 비교
# 4      3       2      1

N = int(input())
for round in range(N):
    # [0] = 카드의 갯수
    A_card = list(map(int, input().split()))[1:]
    B_card = list(map(int, input().split()))[1:]

    for i in range(4, 0, -1):   # 뒤부터 순회
        if A_card.count(i) > B_card.count(i):
            print('A')
            break
        elif A_card.count(i) < B_card.count(i):
            print('B')
            break

        if i == 1:
            print('D')