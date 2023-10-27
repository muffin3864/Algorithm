import sys
sys.stdin = open('input.txt')

# 스도쿠가 겹치는게 없이 들어있는지 확인
# 행, 열 , 작은 배열(3x3) 확인
# 합이 45가 아니면 틀린것

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    # 행 확인
    for i in range(9):
        if sum(arr[i]) != 45:
            result = 0
            break

    # 열 확인
    for i in range(9):
        y_list = []
        for j in range(9):
            y_list.append(arr[j][i])

        if sum(y_list) != 45:
            result = 0
            break

    # 작은 배열 확인
    # 1~3, 4~6, 7~9
    for i in range(0,9,3):
        for j in range(0,9,3):
            small = []
            for x in range(3):
                for y in range(3):
                    small.append(arr[i+x][j+y])
            if sum(small) != 45:
                result = 0
                break

    print(f'#{tc} {result}')

