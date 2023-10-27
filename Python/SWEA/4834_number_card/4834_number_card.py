import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input()))

    count_card = [0] * 10

    for i in card:
        count_card[i] += 1

        result = 0
        num = 0
        for j in range(len(count_card)):
            if count_card[j] >= result:
                result = count_card[j]
                num = j
    print(f'#{tc} {num} {result}')

