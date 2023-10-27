import sys
sys.stdin = open('input.txt')


# 사각형은 0에 둘러쌓여 있음
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    square = {}
    arr = [list(map(int, input().split())) for _ in range(n)]
    for x in range(n):
        cnt = 0
        for y in range(n):
            if arr[x][y] > 0:
                cnt += 1
            elif arr[x][y] == 0 and cnt != 0:
                square[cnt] = square.get(cnt, 0) + 1
                cnt = 0
        if cnt > 0:
            square[cnt] = square.get(cnt, 0) + 1

    matrix = []
    for wide, height in square.items():
        matrix.append((wide * height, height, wide))

    matrix.sort()

    print('#{} {}'.format(tc, len(matrix)), end=' ')
    for i in range(len(matrix)):
        print(matrix[i][1], matrix[i][2], end=' ')
    print()



