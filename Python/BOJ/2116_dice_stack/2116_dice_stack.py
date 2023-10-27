import sys
sys.stdin = open('input.txt')

# 주사위의 맞닿는 윗면과 아랫면이 같은 숫자여야함
# 주사위 탑의 1면의 최대값 구하기

N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]

# 맞닿는 면이 제일 작은 값이여야함
# 마주보는 면 = (0, 5), (1, 3), (2, 4)
plane = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

# 밑면,윗면 설정되면 나머지 값중 가장 큰값이 최대값
sum_dice = 0

# 첫번째 주사위를 기준으로 면 모두 순회
for i in range(6):
    max_dice = []   # 각 주사위 마다 옆면 최대 값
    first_dice = [1, 2, 3, 4, 5, 6]

    # 주사위 아랫면 제거
    first_dice.remove(dice[0][i])

    # 주사위 윗면 찾아서 윗면 제거
    up_side = dice[0][plane[i]]
    first_dice.remove(up_side)

    # 첫번째 주사위 옆면 중 가장 큰 값 넣기
    max_dice.append(max(first_dice))

    # 나머지 주사위
    for j in range(1, N):
        next_dice = [1, 2, 3, 4, 5, 6]
        # 현재 주사위 아랫면 제거
        next_dice.remove(up_side)

        # 현재 주사위 윗면 찾아서 제거
        up_side = dice[j][plane[dice[j].index(up_side)]]
        next_dice.remove(up_side)

        # 현재 주사위 옆면 중 가장 큰 값 넣기
        max_dice.append(max(next_dice))

    # 각 주사위의 최대값 모두 더하기
    max_dice = sum(max_dice)

    # 그 중 제일 큰 값 찾기
    if sum_dice < max_dice:
        sum_dice = max_dice


print(sum_dice)
